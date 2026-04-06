import csv
import time
from datetime import datetime, timezone

import grpc

import send_msg_pb2
import send_msg_pb2_grpc


def run():
    tamanhos = [1, 10000, 100000, 1000000]
    chamadas_por_tamanho = 20

    with open("benchmark.log", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["timestamp", "tamanho_bytes", "indice_chamada", "rtt_ms"])

        print("Conectando ao servidor gRPC...")
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = send_msg_pb2_grpc.SendMsgStub(channel)

            for tamanho in tamanhos:
                print(f"\n--- Iniciando testes para payload de {tamanho} bytes ---")

                # Cria a sequência de bytes para o payload
                payload = b"x" * tamanho
                mensagem = send_msg_pb2.Mensagem(payload=payload)

                for indice in range(1, chamadas_por_tamanho + 1):
                    iniciar_time = time.perf_counter()

                    resposta = stub.Enviar(mensagem)

                    finalizar_time = time.perf_counter()

                    rtt_ms = (finalizar_time - iniciar_time) * 1000

                    timestamp_atual = datetime.now(timezone.utc).isoformat()

                    writer.writerow([timestamp_atual, tamanho, indice, f"{rtt_ms:.2f}"])

                    server_time = resposta.timeStamp.ToJsonString()

                    print(
                        f"Payload: {tamanho:>8} bytes | Chamada: {indice:>2} | RTT: {rtt_ms:>6.2f} ms | Servidor confirmou {resposta.msgLen} bytes às {server_time}"
                    )


if __name__ == "__main__":
    run()
