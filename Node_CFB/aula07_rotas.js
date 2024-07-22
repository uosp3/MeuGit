const express = require("express")
const rotas = express.Router()

let cursosInfo = [
  { curso: "node", info: "Curos de Node" },
  { curso: "react", info: "Curos de React" },
  { curso: "java", info: "Curos de Java" },
  { curso: "arduino", info: "Curos de Arduino" },
]

rotas.get("/", (req, res) => {
  res.json({ ola: "Seja bem-vindo" })
})

rotas.get("/:cursoid", (req, res) => {
  const curso = req.params.cursoid
  const cursoI = cursosInfo.find(
    (i) => i.curso.toUpperCase() == curso.toUpperCase()
  )
  if (!cursoI) {
    res
      .status(404)
      .json({ erro: "Curso não encontrado", cursoPesquisado: curso })
  } else {
    res.status(200).json(cursoI)
  }
})
module.exports = rotas
