;(async () => {
  const db = require("./aula08_db") // nome do arquivo da conexão.

  console.log('Novo cliente inserido')
  const nom='Ailton'
  const ida=34
  await db.insereCliente({nome:nom, idade:ida})

  console.log('Obter todos os clientes')
  const clientes=await db.todosClientes()
  console.log(clientes)
})()
