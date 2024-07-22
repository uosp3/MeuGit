const Sequelize = require('sequelize');
/*conexão com o banco de dados*/
const sequelize = new Sequelize("celke", "root", "", { /*"Base de dados", "root", "senha"*/
    host: 'localhost',
    dialect: 'mysql'
})

sequelize.authenticate() /* função para verificar se a conexão deu certo*/
.then(function(){
    console.log("Conexão com o banco de dados realizada com sucesso!");
}).catch(function(){
    console.log("Erro: Conexão com o banco de dados não realizada com sucesso!");
})

module.exports = sequelize;