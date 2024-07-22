const conectar = async () => {
  if (global.conexao && global.conexao.state != "disconected")
    return global.conexao
  const mysql = require("mysql2/promise")
  const con = mysql.createConnection(
    "mysql://root:My5qldsqto8@localhost:3306/cfbcursos"
  ) // cria a conexão ====> usuário, senha, host, porta, banco
  console.log("Conectou ao banco")
  global.conexao = con
  return con
}

const todosClientes = async () => {
  const con = await conectar()
  const [linhas] = await con.query("SELECT * FROM cliente_node")
  return await linhas
}

const insereCliente = async (cliente) => {
  const con = await conectar()
  const sql = "insert into cliente_node (nome, idade) values (?,?)"
  const valores = [cliente.nome, cliente.idade]
  await con.query(sql, valores)
}

const atualizaCliente = async (id, cliente) => {
  const con = await conectar()
  const sql = "update cliente_node set nome=?, idade=? where id=?"
  const valores = [cliente.nome, cliente.idade, id]
  await con.query(sql, valores)
}

const deletarCliente = async (id) => {
  const con = await conectar()
  const sql = "delete from cliente_node where id=?"
  const valores = [id]
  await con.query(sql, valores)
}

module.exports = {
  todosClientes,
  insereCliente,
  atualizaCliente,
  deletarCliente,
}
