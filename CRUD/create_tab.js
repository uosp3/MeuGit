//funcionando, não mexer
const Sequelize = require("sequelize");
const conexao = new Sequelize("test", "root", "", {
  dialect: "mysql",
  host: "localhost",
});
//cria a tabela
(async () => {
  const Produto = conexao.define("artigo", {
    id: {
      type: Sequelize.INTEGER,
      autoIncrement: true,
      allowNull: false,
      primaryKey: true,
    },
    nome: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    preco: {
      type: Sequelize.DOUBLE,
    },
    descricao: Sequelize.STRING,
  });

  try {
    const resultado = await conexao.sync();
    console.log("Criando tabela...");
  } catch (error) {
    console.log(error);
  }
})();
