//gravar dados, funcionando, não mexer
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
    const resultadoCreate = await Produto.create({
      nome: "impressora2",
      preco: 1000,
      descricao: "Epson L355",
    });
    console.log("Gravando dados...");
  } catch (error) {
    console.log(error);
  }
})();
