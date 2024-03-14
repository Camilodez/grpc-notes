# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import notas_pb2 as notas__pb2


class NotasServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CalcularNotaFinal = channel.unary_unary(
                '/notas.NotasService/CalcularNotaFinal',
                request_serializer=notas__pb2.SolicitudNotas.SerializeToString,
                response_deserializer=notas__pb2.RespuestaNotaFinal.FromString,
                )


class NotasServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CalcularNotaFinal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NotasServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CalcularNotaFinal': grpc.unary_unary_rpc_method_handler(
                    servicer.CalcularNotaFinal,
                    request_deserializer=notas__pb2.SolicitudNotas.FromString,
                    response_serializer=notas__pb2.RespuestaNotaFinal.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notas.NotasService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NotasService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CalcularNotaFinal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notas.NotasService/CalcularNotaFinal',
            notas__pb2.SolicitudNotas.SerializeToString,
            notas__pb2.RespuestaNotaFinal.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
