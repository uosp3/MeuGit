//https://www.youtube.com/watch?v=zfLQz2HA4s4
function f_teste<T,U>(v:T,r:U):U{
    return r
}

console.log(f_teste<number,string>(10,"B"))
console.log(f_teste<string,number>("B",10))
console.log(f_teste<boolean,boolean>(true,false))

class C_teste<T>{
    public valor:T
    constructor(valor:T){
        this.valor=valor
    }
}

const ct1=new C_teste<number>(100)
const ct2=new C_teste<string>("111")

console.log(ct1.valor)
console.log(ct2.valor)