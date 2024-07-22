let num = [5,8,2,9,3,200]
num.push(7)
console.log(num.length)
num.sort() //ordem alfa
num.sort(Number) //ordem numérica
//num.sort(function(a,b){return a-b})// ordem numérica tb
console.log(`Nosso vetor é o ${num} ele tem ${num.length} posições`)
console.log(num)

let pos = num.indexOf(4)
if (pos != -1){
console.log(`O valor 8 está na posição ${pos}`)
} else {
    console.log(`O valor não foi enontrado`)
}

