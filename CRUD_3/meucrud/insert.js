(async()=>{
    const database = require('../db');
    const Produto = require('../models/produto');
    
try{       
        const resultadoCreate = await Produto.create({
            nome: 'mouse140',
            preco: 14,
            descricao: 'Um mouse14 USB legal'
        })
        console.log("Dados cadastrados com sucesso!")
        //console.log(resultado);        
    } catch (error){
        console.log(error);
    }
})();