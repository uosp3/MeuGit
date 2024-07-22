(async()=>{
    const database = require('../db');
    const Produto = require('../models/produto');
    
try{      
   Produto.destroy({where: { id: 3}})
   console.log("Produto excluido com sucesso!")

    // pode ser feito de duas formas, conforme acima ou conforme abaixo (da forma abaixo da erro se não for encontrado.)
    
//    const produto = await Produto.findByPk(2);
//    produto.destroy();
//    console.log("Produto excluido com sucesso!")

}catch (error){
    console.log(error)
}

})();