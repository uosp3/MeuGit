(async()=>{
    const database = require('../db');
    const Produto = require('../models/produto');
    
try{      
   const produtos = await Produto.findByPk(1);// consulta e retorna apenas o produto de chave = 1 para em seguida fazer a alteração.
   console.log(produtos.preco);
   produtos.descricao = "Fone sem fio";

   const alterar = await produtos.save();  
    console.log("Ateração feita com sucesso!")

}catch (error){
    console.log(error)
}

})();