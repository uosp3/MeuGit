"use strict";
let av = [10, 20, 30, 40];
let [aa, bb, cc, dd] = av;
//ou conforme linha abaixo
//let [aa,bb,cc,dd]=[10,20,30,40]
console.log(aa);
console.log(bb);
console.log(cc);
console.log(dd);
//com um objeto
const obj = {
    cor1: "verde",
    cor2: "Amarelo",
    cor3: "Azul",
    cor4: "Branco"
};
let { cor1, cor2, cor3, cor4 } = obj;
console.log(cor1);
console.log(cor2);
console.log(cor3);
console.log(cor4);
