(async()=>{
    const database = require('../db');
    const Produto = require('../models/produto');
    
try{       
    // const produtos = await Produto.findAll();// consulta a tabela e retorna todos os produtos
    // console.log(produtos);

    // const produtos = await Produto.findByPk(1);// consulta e retorna apenas o produto de chave = 1
    // console.log(produtos.descricao)

    const produtos = await Produto.findAll({
        where:{
            preco: 10000 // consulta a tabela e retorna produto de preço = 
        }
    });
    console.log(produtos);


}catch (error){
    console.log(error)
}

})();