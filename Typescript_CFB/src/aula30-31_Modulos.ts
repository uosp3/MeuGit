//https://www.youtube.com/watch?v=-bZyA_2-5PM
import Pessoa, {Objeto, Coisas } from "./aula30_Classes"; //Pessoa ficou fora das chaves por ter sido exportado por "default". Vide arquivo "aula30_Classe.ts"

const p1=new Pessoa("Edson", 1.64)
const o1=new Objeto("Mesa")

console.log(p1.nome)
console.log(p1.altura)
console.log(Coisas)