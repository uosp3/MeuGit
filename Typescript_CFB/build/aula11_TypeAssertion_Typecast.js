"use strict";
//https://www.youtube.com/watch?v=QC59ZXoe83c - vídeo da aula.
let nvalor;
let svalor;
let uvalor;
uvalor = 10;
svalor = '20';
nvalor = uvalor; //é necessário afirmar que uvalor é number, caso contrário da erro.
//nvalor=<number>svalor; //A conversão do tipo 'string' para o tipo 'number' pode ser um erro porque nenhum tipo está suficientemente sobreposto ao outro. Se isso era intencional, converta a expressão para 'unknown' primeiro. Conforme linha abaixo
nvalor = svalor;
//para converter string em number - nvalor=Number.parseInt(svalor);
//para converter number em string - svalor=nvalor.toString()
svalor = uvalor;
svalor += 10;
console.log(typeof (uvalor));
console.log(uvalor);
console.log(typeof (nvalor));
console.log(nvalor);
console.log(typeof (svalor));
console.log(svalor);
