import grpc
import notas_pb2
import notas_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = notas_pb2_grpc.NotasServiceStub(channel)
        response = stub.CalcularNotaFinal(
            notas_pb2.SolicitudNotas(
                nota1=4.5, porcentaje1=0.3,
                nota2=3.8, porcentaje2=0.3,
                nota3=4.2, porcentaje3=0.4
            )
        )
        print("Nota final calculada: {:.2f}".format(response.notaFinal))

if __name__ == '__main__':
    run()
