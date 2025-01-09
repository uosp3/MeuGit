// https://www.youtube.com/watch?v=V3PUGubaSQo&list=PLnex8IkmReXwCyR-cGkyy8tCVAW7fGZow&index=2
// const express = require('express')
import express from 'express' //linha acima convertida em ES
const app = express()

// mock
const selecoes = [
  {id:1, selecao: 'Brasil', grupo: 'G'},
  {id:2, selecao: 'Suíça', grupo: 'G'},
  {id:3, selecao: 'Sérvia', grupo: 'G'},
  {id:4, selecao: 'Camarões', grupo: 'G'},
]

// criar rota padrão ou raiz
app.get('/', (req, res) => {
  res.send('Curso de Node JS..')
})

app.get('/selecoes', (req,res) => {
  res.status(200).send(selecoes)
})

// // escutar a porta 3000
// app.listen(port, () => {
//   console.log(`Servidor rodando no endereço http://localhost:${port}`)
// })

export default app

