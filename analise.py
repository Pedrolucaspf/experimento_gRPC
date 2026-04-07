import pandas as pd
import matplotlib.pyplot as plt


def gerar_grafico():
    print("Lendo o arquivo benchmark.log...")

    try:
        df = pd.read_csv("benchmark.log")

        medias_rtt = df.groupby("tamanho_bytes")["rtt_ms"].mean().reset_index()
        print("\nMédia de RTT por tamanho de payload:")
        print(medias_rtt)

        tamanhos = medias_rtt["tamanho_bytes"].astype(str)
        rtt_medio = medias_rtt["rtt_ms"]

        plt.figure(figsize=(10, 6))
        barras = plt.bar(tamanhos, rtt_medio)

        plt.xlabel("Tamanho do Payload (bytes)")
        plt.ylabel("RTT Médio (ms)")
        plt.title("RTT Médio por Tamanho de Payload via gRPC")

        for barra in barras:
            altura = barra.get_height()
            plt.text(
                barra.get_x() + barra.get_width() / 2.0,
                altura,
                f"{altura:.2f} ms",
                ha="center",
                va="bottom",
            )

        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(
            "Arquivo benchmark.log não encontrado. Execute o cliente para gerar os dados primeiro."
        )
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


if __name__ == "__main__":
    gerar_grafico()
