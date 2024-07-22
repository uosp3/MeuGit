// código não apresenta erro mas os dados não são inserigos no Mongodb ?????????

const mongodb = require("mongodb").MongoClient
const url ="mongodb+srv://uosp3:M0ng0dbdsqto8@cluster0.sqgcekd.mongodb.net/?retryWrites=true&w=majority"
mongodb.connect(url, (erro, banco) => {
  console.log("chegou até aqui")
  if (erro) throw erro
  const dbo = banco.db("cfbcursos")
  const obj = { curso: "Curso de Node", canal: "CFB Cursos" }
  const colecao = "cursos"
  dbo.collection(colecao).insertOne(obj, (erro, resultado) => {
    if (erro) throw erro
    console.log("1 novo curso inserido")
    banco.close()
  })
})
