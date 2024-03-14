from concurrent import futures
import grpc
import notas_pb2
import notas_pb2_grpc

SERVER_1_ADDRESS = 'localhost:50051'
SERVER_2_ADDRESS = 'localhost:50052'

class ServidorCentralServicer(notas_pb2_grpc.NotasServiceServicer):
    def CalcularNotaFinal(self, request, context):
        try:
            with grpc.insecure_channel(SERVER_1_ADDRESS) as channel1:
                stub1 = notas_pb2_grpc.NotasServiceStub(channel1)
                response = stub1.CalcularNotaFinal(request)
                return response
        except grpc.RpcError as e1:
            print("No se pudo conectar con el Servidor 1. Intentando con el Servidor 2. Error:", e1)

        try:
            with grpc.insecure_channel(SERVER_2_ADDRESS) as channel2:
                stub2 = notas_pb2_grpc.NotasServiceStub(channel2)
                response = stub2.CalcularNotaFinal(request)
                return response
        except grpc.RpcError as e2:
            print("No se pudo conectar con el Servidor 2. Calculando en el Servidor Central. Error:", e2)

        # Si ambos servidores se caen, realiza el cálculo en el servidor central
        print("Ambos servidores están caídos. Realizando cálculo en el Servidor Central.")
        return self.calcular_nota_final_localmente(request)

    def calcular_nota_final_localmente(self, request):
        suma_ponderada = (request.nota1 * request.porcentaje1 +
                          request.nota2 * request.porcentaje2 +
                          request.nota3 * request.porcentaje3)
        nota_final_redondeada = round(suma_ponderada, 2)
        return notas_pb2.RespuestaNotaFinal(notaFinal=nota_final_redondeada)

       
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notas_pb2_grpc.add_NotasServiceServicer_to_server(ServidorCentralServicer(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
