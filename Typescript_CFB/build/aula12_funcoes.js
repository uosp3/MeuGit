"use strict";
function logar(user, pass) {
    console.log(`User.: ${user}`);
    console.log(`Senha: ${pass}`);
}
logar("Edson", "123"); //função sem retorno
function soma2(n1, n2) {
    return n1 + n2;
}
const n_res = soma2(10, 5); //a função com retorno precisa que o valor do retorno seja atribuido a algo.
const s_res = soma2(2, 8).toString();
console.log(n_res);
console.log(s_res);
