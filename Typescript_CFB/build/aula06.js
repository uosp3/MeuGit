"use strict";
let numeros = [20, 30, 40];
//ou
let numeros2 = [20, 30, 40, "Edson"];
//ou
let numeros3 = [20, 30, 40, "Edson"];
numeros.push(50); //insere no final do array
numeros.unshift(10); //insere no inicio do array
numeros.pop(); //exclui no final do array
numeros.shift(); //exclui no inicio do array
console.log(numeros);
let numeros_ro = [100, 200, 300]; //array somente leitura
