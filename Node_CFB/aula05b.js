const http = require("http")
const fs = require("fs")
const porta = process.env.PORT

const server = http.createServer((req, res) => {
  fs.appendFile(
    "aula05.txt",
    "Arquivo criado pela aula05b.js  =  Curso de Node - CFB Cursos",
    (err) => {
      //cria o aquivo aula05.txt
      if (err) throw err
      console.log("Arquivo criado")
      res.end()
    }
  )
})

server.listen(porta || 3000, () => {
  console.log("Servidor Rodando")
})
