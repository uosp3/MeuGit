;(async () => {
  const db = require("./aula08_db") // nome do arquivo da conexão.

  const id = 2  
  await db.deletarCliente(id)
  console.log("Cliente " + id + "  deletado")

  console.log("Obter todos os clientes")
  const clientes = await db.todosClientes()
  console.log(clientes)
})()

