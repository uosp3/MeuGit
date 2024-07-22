const Sequelize = require('sequelize');
const sequelize = new Sequelize('crud_3', 'root', '',{
    dialect: 'mysql',
    host: 'localhost',
    port: 3306
})

module.exports = sequelize;
