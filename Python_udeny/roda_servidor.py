#  colaboração chatGPT
#  PARA RODAR O SERVIDOR DE TESTES
from flask import Flask

app = Flask(__name__)


# Rota básica de exemplo
@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    # Defina a porta desejada aqui
    porta = 8000
    app.run(port=porta)
