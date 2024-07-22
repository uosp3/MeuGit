//uma arrow function não pode ser chamada sem que ainda não tenhas sido criada, o contrário de uma function que pode ser criada em qualquer parte do código e ser chamada mesmo antes da criação.
//uma arrow function tem que ser associada a uma variável ou uma constante

const teste=(txt:string):void=>{
    console.log(txt);
}

const fsoma2=(n1:number, n2:number):number=>{
    return n1+n2
}

const fsoma3=(n:number[]):number=>{
    let s:number=0;
    n.forEach((e)=>{
        s+=e;
    })
    return s;
}

teste("CFBCursos");
console.log(fsoma2(90,10));

let numer:number[]=[10,20,30,40,50]
console.log(fsoma3(numer))
