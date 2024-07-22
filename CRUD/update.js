//funcionando, não mexer
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
   
    const produto = await Produto.findByPk(2);
    //console.log(produto);
    produto.nome = "Mouse Top2"
    produto.preco = 55
    produto.descricao = 'Mouse novo'
     
    const resultadoSave = await produto.save();
    console.log(resultadoSave);

    console.log("Alterando dados...");
  } catch (error) {
    console.log(error);
  }
})();
