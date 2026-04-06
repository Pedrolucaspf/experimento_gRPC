import grpc
from concurrent import futures
import send_msg_pb2
import send_msg_pb2_grpc
from datetime import datetime, timezone
from google.protobuf.timestamp_pb2 import Timestamp


class SendMsgServicer(send_msg_pb2_grpc.SendMsgServicer):
    def Enviar(self, request, context):
        messageLength = len(request.payload)

        timeNow = datetime.now(timezone.utc)
        time_iso = timeNow.isoformat()

        tempo_pb = Timestamp()
        tempo_pb.FromDatetime(timeNow)

        print(f"[servidor] Recebido payload de {messageLength} bytes em {time_iso}")

        return send_msg_pb2.Confirmacao(msgLen=messageLength, timeStamp=tempo_pb)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    send_msg_pb2_grpc.add_SendMsgServicer_to_server(SendMsgServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
