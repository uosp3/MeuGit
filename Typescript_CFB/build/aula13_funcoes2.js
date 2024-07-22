"use strict";
function soma(n1 = 0, n2 = 0) {
    return n1 + n2;
}
console.log(soma(5)); //o segundo parâmetro não foi informado e foi assumido como zero que foi definido na criação da função.
function novoUser(user, pass, nome) {
    let dados = { user, pass, nome };
    console.log(dados);
}
novoUser("br", '123');
