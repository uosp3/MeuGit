let dados={
    nome:"Edson",
    idade: 61,
    status:"A",
    ola:()=>{console.log("Oi")},
    info:(p:string)=>{console.log(p)}
}

dados.nome="Gomes"

console.log(typeof(dados));
console.log(dados.nome);

dados.ola();
dados.info(dados.nome);