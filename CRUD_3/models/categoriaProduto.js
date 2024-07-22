const Sequelize = require('sequelize');
const database = require('../db');

const CategoriaProduto = database.define('categoriaProduto', {//criar a tabela
    id:{//campos da tabela
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    }
});

module.exports = CategoriaProduto;