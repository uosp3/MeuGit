//ler dados, funcionando, não mexer
const Sequelize = require("sequelize");
const conexao = new Sequelize("test", "root", "", {
  dialect: "mysql",
  host: "localhost",
});

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
    const produtos = await Produto.findAll({
      where: { preco: 100}
  });
    console.log(produtos);
    console.log("Lendo dados...");
  } catch (error) {
    console.log(error);
  }
})();
