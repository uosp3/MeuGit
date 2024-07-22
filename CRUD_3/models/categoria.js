const Sequelize = require('sequelize');
const database = require('../db');

const Categoria = database.define('categoria', {//criar a tabela
    id:{//campos da tabela
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    nome: {
        type: Sequelize.STRING,
        allowNull: false
    },
});

module.exports = Categoria;