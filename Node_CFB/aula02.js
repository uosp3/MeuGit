const http = require("http")

http
  .createServer((requisicao, resposta) => {
    resposta.writeHead(200, {
      "Content-Type": "text/plain",
    })
    resposta.write("CFB Cursos\nCurso de Node.js")
    resposta.end()
  })
  .listen(1337)
  // abrir o terminal, acessar o caminho do arquivo e digitar: node aula02.js -> ativa o servidor
  // abra o navegador e acesse: localhost:1337

