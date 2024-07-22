//Nulo, indefinido e desconhecido
let vnome:string|null;
vnome=null;
console.log(vnome); //imprime null

let vnome2;
console.log(vnome2);//imprime indefined, o valor não foi associado

let vnome3:unknown=vnome; //unknown só pode ser atribuido em tipos unknown ou any
let vnum:any=vnome3;
console.log(vnum);