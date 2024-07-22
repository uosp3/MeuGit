//https://www.youtube.com/watch?v=tfqE3ncgovs
interface curso{ //com a "interface" pode se usar o objeto sem ter que criar um novo.
    titulo:string;
    des:string;
    iniciarCurso?(teste:string):void;
}

interface cursoProg extends curso{
    aulas:number;
    maxAlunos?:number;//A "?" faz com que o item não seja obrigatorio quando
}

interface cursoArtes extends curso{
    aulas:number;
    maxAlunos?:number;//A "?" faz com que o item não seja obrigatorio quando
}

let curso1:cursoProg
let curso2:cursoProg
let curso3:cursoArtes

curso1={
    titulo:"Typescript",
    des:"Curso de Tupescritp",
    aulas:100,
    maxAlunos:50,
}

curso2={
    titulo:"Javascript",
    des:"Curso de Javascritp", 
    aulas:200, 
    maxAlunos:80
}

curso3={
    titulo:"C++", 
    des:"Curso de c++", 
    aulas:200
}//nesse caso o maxAlunos foi omitido, pois ele é opcional.

console.log(curso1)
console.log(curso2)
console.log(curso3)