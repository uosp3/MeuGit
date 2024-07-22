const Sequelize = require('sequelize');
const database = require('../db');

const Fabricante = database.define('fabricante', {//criar a tabela
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

module.exports = Fabricante;