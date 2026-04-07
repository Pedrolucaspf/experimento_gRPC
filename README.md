# Experimento gRPC - Sistemas Distribuídos

Este projeto é um experimento prático utilizando **gRPC** em Python para a disciplina de Sistemas Distribuídos. O gerenciamento de dependências e ambientes virtuais é feito com o [uv](https://github.com/astral-sh/uv).

## Pré-requisitos

Para rodar este projeto, você precisa ter instalado:
- **Python 3.12+**
- **uv**: Pode ser instalado via curl no Linux/WSL:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## Instalação das dependências

Na raiz do projeto, instale as bibliotecas necessárias (gRPC, Protobuf e Matplotlib) executando:

```bash
uv sync
```


## Como executar a aplicação

O sistema é composto por um Servidor e um Cliente gRPC. 

### 1. Inicie o Servidor
Abra um terminal e execute o servidor. Ele ficará escutando as requisições do cliente.
```bash
uv run python server.py
```

### 2. Inicie o Cliente
Com o servidor rodando, abra **outro terminal** e execute o cliente para enviar as mensagens:
```bash
uv run python client.py
```

### 3. Rodar Análise / Benchmarks (Opcional)
Se precisar gerar os gráficos com o `matplotlib` ou obter relatórios e logs, você pode rodar script de análise:
```bash
uv run python analise.py
```

## Como gerar os arquivos gRPC (Opcional)

Se você alterar o arquivo `send_msg.proto`, será necessário gerar novamente o código Python do gRPC (arquivos `_pb2.py` e `_pb2_grpc.py`). 

Para isso, utilize a ferramenta do `grpc_tools` através do `uv`:
```bash
uv run python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. send_msg.proto
```
