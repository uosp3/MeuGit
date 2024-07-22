;(async () => {
  const db = require("./aula08_db") // nome do arquivo da conexão.

  const id = 2
  const nom = "Edson Gomes"
  const ida = 62
  await db.atualizaCliente(id, { nome: nom, idade: ida })
  console.log("Cliente " + id + " atualizado")

  console.log("Obter todos os clientes")
  const clientes = await db.todosClientes()
  console.log(clientes)
})()

