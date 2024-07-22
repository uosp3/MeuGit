const Sequelize = require('sequelize');
const db = require('./db')

const User = db.define('users',{ /* cria a tabela users*/
    id: { /* campo da tabela */
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    name: {  /* campo da tabela */
        type: Sequelize.STRING,
        allowNull: false,
    },
    email: {  /* campo da tabela */
        type: Sequelize.STRING,
        allowNull: false,
    },
});

//criar a tabela (depois que a linha abaixo foi executada ela foi comentada para não tentar criar novamente a tabela)
//User.sync();
//Verifica se há alguma diferença na tabela, realiza a alteração
//User.sync({alter: true})

module.exports = User;