abstract class Conta{ //classe não pode ser instanciada. Serve somente para ser extendida/herdada
//https://www.youtube.com/watch?v=Q73LywpCSLk
//https://www.youtube.com/watch?v=Q73LywpCSLk&list=PLx4x_zx8csUhtPMrkiGvFJVE5LX8Qat5s&index=26

    private readonly numero:number //readonly não permite alteração do nr da conta
    protected titular:string
    private saldoconta:number
    constructor(titular:string){
        this.numero=this.gerarNumeroConta()
        this.titular=titular
        this.saldoconta=0
    }
    private gerarNumeroConta():number{
        return Math.floor(Math.random()*100000)+1
    }
    protected info(){
        console.log(`Titular: ${this.titular}`)
        console.log(`Número: ${this.numero}`)
    }
    get saldo():number{ //Getter
        return this.saldoconta
    }
    private set saldo(saldoconta:number){//Setter
        this.saldoconta=saldoconta
    }
    protected deposito(valor:number){
        if(valor<0){
            console.log(`Valor inválido`)
            return
        }
        this.saldo+=valor
    }
    protected saque(valor:number){
        if(valor<0){
            console.log(`Valor inválido`)
            return
        }
        if(valor<=this.saldoconta){
            this.saldo-=valor
        }else{
            console.log(`Saldo insuficionete`)
        }
    }
}
//https://www.youtube.com/watch?v=tfqE3ncgovs alteração feita nesse vídeo, instante 9:00 **

interface Tributos{
    taxaCalculo:number;
    CalcularTrib(valor:number):number;
}

class ContaPF extends Conta implements Tributos{
    taxaCalculo=10;//**
    cpf:number
    constructor(cpf:number,titular:string){
        super(titular)
        this.cpf=cpf
    }
    CalcularTrib(valor:number):number{//**
        return valor*this.taxaCalculo
    }
    info(){
        console.log(`Tipo...:PF`)
        super.info()
        console.log(`CPF....: ${this.cpf}`)
        console.log(`---------------------`)
    }
    public deposito(valor:number){
        if(valor>1000){
            console.log(`Valor de depósito muito grande para este tipo de conta`)
        }else{
            super.deposito(valor)
        }
    }
    public saque(valor:number){
        if(valor>1000){
            console.log(`Valor de saque muito grande para este tipo de conta`)
        }else{
            super.saque(valor)
        }
    }
}

class ContaPJ extends Conta{
    cnpj:number
    constructor(cnpj:number,titular:string){
        super(titular)
        this.cnpj=cnpj
    }
    info(){
        console.log(`Tipo...:PJ`)
        super.info()
        console.log(`CNPJ...: ${this.cnpj}`)
        console.log(`---------------------`)
    }
    public deposito(valor:number){
        if(valor>10000){
            console.log(`Valor de depósito muito grande para este tipo de conta`)
        }else{
            super.deposito(valor)
        }
    }
    public saque(valor:number){
        if(valor>10000){
            console.log(`Valor de saque muito grande para este tipo de conta`)
        }else{
            super.saque(valor)
        }
    }
}

const cont1=new ContaPF(111, "Edson")
const cont2=new ContaPJ(222333, "Gomes")

//console.log(cont1.titular)
//console.log(cont1.numero)

cont1.deposito(800)
cont1.deposito(200)
cont1.deposito(1000)
//cont1.saque(1000)
//cont1.saque(500)
//cont1.saque(500)
//cont1.saque(10)
console.log(cont1.saldo)

// cont2.deposito(10000)
// cont2.deposito(10000)
// cont2.deposito(10000)
// cont2.deposito(10000)
// console.log(cont2.saldo())

cont1.info()
//cont2.info()

