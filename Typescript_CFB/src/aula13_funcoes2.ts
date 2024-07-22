function soma(n1:number=0, n2:number=0):number{ //foram atribuidos volores padrão, caso não seja passado o parâmetro será adotado zero.
    return n1+n2
}

console.log(soma(5))//o segundo parâmetro não foi informado e foi assumido como zero que foi definido na criação da função.

function novoUser(user:string, pass:string, nome?:string):void{//a interrogação no parâmetro "nome" indica que ele é opcional, pode ou não ser passado na chamada da função
    let dados={user, pass, nome}
    console.log(dados)
}

novoUser("br",'123')