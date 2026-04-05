import grpc
from concurrent import futures
import send_msg_pb2
import send_msg_pb2_grpc
from datetime import datetime, timezone
from google.protobuf.timestamp_pb2 import Timestamp

class SendMsgServicer(send_msg_pb2_grpc.SendMsgServicer):
    def Enviar(self, request, context):
        messageLength = len(request)
        tempo = Timestamp()
        tempo_iso = tempo.ToDatetime().isoformat()
        tempo.FromDatetime(datetime.now(timezone.utc))
        print(f"[servidor] Recebido payload de {messageLength} bytes em {tempo_iso}")
        return send_msg_pb2.Confirmacao(
            msgLen = messageLength,
            location=tempo_iso
        )


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    send_msg_pb2_grpc.add_SendMsgServicer_to_server(SendMsgServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()
