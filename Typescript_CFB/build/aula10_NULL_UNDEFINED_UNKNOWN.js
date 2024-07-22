"use strict";
//Nulo, indefinido e desconhecido
let vnome;
vnome = null;
console.log(vnome); //imprime null
let vnome2;
console.log(vnome2); //imprime indefined, o valor não foi associado
let vnome3 = vnome; //unknown só pode ser atribuido em tipos unknown ou any
let vnum = vnome3;
console.log(vnum);
