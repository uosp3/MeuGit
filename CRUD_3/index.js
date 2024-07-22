//index.js
(async()=>{
    const database = require('./db');
    const Produto = require('./models/produto');
    const Fabricante = require('./models/fabricante');
    const Categoria = require('./models/categoria');
    await database.sync();

        //gravar dados na(s) tabela(s)////////////////////////////////////////////////////////
        const inserir = false; // gravar ou não os dados na tabela.
        if (inserir){
            const NomeFabricante = "Apple71"
            const existe = await Fabricante.findOne({
                where:{
                    nome: NomeFabricante // ver se fabricante ja existe.
                }
            });
            if (existe===null){ //se não existe grava nas duas tabelas.
                const novoFabricante = await Fabricante.create({//insere dados na tabela "Fabricante"
                    nome: NomeFabricante
                })                
                const novoProduto =await Produto.create({//insere dados na tabela "Produto"
                    nome: "Onze171a",
                    preco: 15000,
                    descricao: "Notebook",
                    idFabricante: novoFabricante.id
                })            
                console.log ("Dados gravados com sucesso!") 
            }else{ //se existe, grava apenas o produto.
                const novoProduto =await Produto.create({//insere dados na tabela "Produto"
                    nome: "Onze2",
                    preco: 1001,
                    descricao: "Notebook da Apple",
                    idFabricante: existe.id
                }) 
                console.log ("Dados gravados com sucesso!")            
            }            
        }else{
            console.log ("Nada foi gravado.................................")
        }
        //Fim - gravar dados na(s) tabela(s)////////////////////////////////////////////////////////

        //Com o relacionamento (1:1) das tabelas, pegar o nome do fabricante a partir de um produto. É chamado de Lazy Loading (carregamento tardio)
        const produtos = await Produto.findByPk(20)
        const fabricante = await produtos.getFabricante()
        console.log(fabricante.nome)
        console.log("***********************************************************")

        // Outra opção é ja pegar o nome do fabricante a partir de parâmetros da primeira consulta. É chamado de Eager Loading
        const produtos2 = await Produto.findByPk(3, { include: Fabricante });
        console.log(produtos2.fabricante.nome)
        console.log("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        //Com o relaciomento (1:N) das tabelas, pegar os produtos de um determinado fabricante.
        const fabricante3 = await Fabricante.findByPk(14);
        const produtos3 = await fabricante3.getProdutos();
        console.log(produtos3)
        console.log("...............................................................")

        // ou assim:
        const fabricante4 = await Fabricante.findByPk(14, {include: Produto});
        console.log(fabricante4.produtos);

        //Com o relacionamento N:N
        const novaCategoria = await Categoria.create({nome: 'informatica2'});
        const produto = await Produto.findByPk(18);
        await produto.setCategoria([novaCategoria]);

})();

//documentação oficial:
//https://sequelize.org/docs/v6/core-concepts/model-querying-finders/#-code-findall--code-

//vídeo explicativo
//https://www.youtube.com/watch?v=vJZ_kh7G8-k