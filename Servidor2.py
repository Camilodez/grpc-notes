from concurrent import futures
import grpc
import notas_pb2
import notas_pb2_grpc

class Servidor2Servicer(notas_pb2_grpc.NotasServiceServicer):
    def CalcularNotaFinal(self, request, context):
        suma_ponderada = (request.nota1 * request.porcentaje1 +
                          request.nota2 * request.porcentaje2 +
                          request.nota3 * request.porcentaje3)
          
        nota_final_redondeada = round(suma_ponderada, 2)
        print(f"Suma ponderada calculada en el Servidor 1: {nota_final_redondeada}")
        return notas_pb2.RespuestaNotaFinal(notaFinal=nota_final_redondeada)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notas_pb2_grpc.add_NotasServiceServicer_to_server(Servidor2Servicer(), server)
    server.add_insecure_port('[::]:50052')  # Puerto para el servidor 2
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
