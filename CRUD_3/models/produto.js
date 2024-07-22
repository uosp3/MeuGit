const Sequelize = require('sequelize');
const database = require('../db');
const Fabricante = require('./fabricante');
const CategoriaProduto = require('./categoriaProduto');
const Categoria = require('./categoria');

const Produto = database.define('produto', {//criar a tabela
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
    preco: Sequelize.DOUBLE,
    descricao: Sequelize.STRING
});

Produto.belongsTo(Fabricante, { // para relacionamento 1:1
    constraint: true,
    foreignKey: "idFabricante" //chave extrangeira
})

Fabricante.hasMany(Produto, { // para relacionamentos 1:N
    foreignKey: 'idFabricante' //chave extrangeira
})

Produto.belongsToMany(Categoria, { // para relacionamentos N:N - A partir dos produtos chegar na categoria
    through:{ //o relacionamento será feito através da tabela "CategoriaProduto"
        model: CategoriaProduto
    },
    foreignKey: 'idProduto',//chave extrangeira
    constraint: true
})

Categoria.belongsToMany(Produto, { // para relacionamentos N:N - A partir da categoria chegar nos produtos
    through:{  //o relacionamento será feito através da tabela "CategoriaProduto"
        model: CategoriaProduto
    },
    foreignKey: 'idCategoria',//chave extrangeira
    constraint: true
})

// Super muitos para muitos - Super Many-To-Many Relationship
Produto.hasMany(CategoriaProduto, { foreignKey: 'idProduto'}) // um protudo tem muitos da tabela 'meio'
CategoriaProduto.belongsTo(Produto, { foreignKey: 'idProduto'}) // a tabela 'meio' pertence ao produto
Categoria.hasMany(CategoriaProduto, { foreignKey: 'idCategoria'})// a tabela à direita do relac. tem muitos da tabela 'meio'
CategoriaProduto.belongsTo(Categoria, { foreignKey: 'idCategoria'})// a tabela meio pertence à tabela da direita

module.exports = Produto;