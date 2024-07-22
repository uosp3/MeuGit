
let av=[10,20,30,40]
let [aa,bb,cc,dd]=av

//ou conforme linha abaixo
//let [aa,bb,cc,dd]=[10,20,30,40]

console.log(aa)
console.log(bb)
console.log(cc)
console.log(dd)

//com um objeto
const obj={
    cor1:"verde",
    cor2:"Amarelo",
    cor3:"Azul",
    cor4:"Branco"
}

let {cor1,cor2,cor3,cor4}=obj

console.log(cor1)
console.log(cor2)
console.log(cor3)
console.log(cor4)

//passando valores incompletos
let [nu1=0,nu2=0,nu3=0]=[10]
console.log(nu1)
console.log(nu2)
console.log(nu3)

//passando valores a mais e fazendo spred
let [nu4=0,nu5=0,...nu6]=[10,20,30,40,50,60,70,80,90]
console.log(nu4)
console.log(nu5)
console.log(nu6)

//usando uma função
const fcores=()=>{
    return ["verde","Amarelo", "Azul", "Branco"]
}

let [co1,co2,co3,co4]=fcores()
console.log(co1)
console.log(co2)
console.log(co3)
console.log(co4)

//desestruturando um texto
let texto="Curso de Typescript"
let [...t]=texto.split(" ")
let [p1,p2,p3]=texto.split(" ")


console.log(t)
console.log(p1)
console.log(p2)
console.log(p3)