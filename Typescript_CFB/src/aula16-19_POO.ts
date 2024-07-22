class Computador{
    private id:number;
    public nome:string; //public é facultativo(é o padrão), não precisa ser definido
    private ram:number;
    private cpu:number;
    protected ligado:boolean;
    //public - pode ser alterado de qualquer lugar
    //private - so pode alterar pela própria classe
    //protected - pode alterar tb pelas classes filhas.

    constructor(n:string, ram:number, cpu:number){
        this.nome=n;
        this.ram=ram;
        this.cpu=cpu;
        this.ligado=false;
        this.id=0;        
    }
    
    info():void{
        console.log(`Nome..:${this.nome}`)
        console.log(`Ram...:${this.ram}`)
        console.log(`CPU...:${this.cpu}`)
        console.log(`Ligado:${this.ligado?"Sim":"Não"}`)
        console.log(`---------------`)
    }

    ligar():void{
        this.ligado=true;
    }
    desligar():void{
        this.ligado=false;
    }

    upRam(qtde:number):void{
        if(qtde >= 0 && qtde <=1000){
            this.ram=qtde;
        }else{
            console.log(`Quantidade ${qtde} para o computador ${this.nome} não é permitida`)
        }
    }
}

//Instanciar a classe - Cria o objeto da classe
const comp1=new Computador('Rapidão',64,10);
const comp2=new Computador('Carão',32,5);
const comp3=new Computador('Gamer',128,10);

comp1.ligar();// a propriedade "ligado" so pode ser acessada pelo método "ligar" ou "desligar" pois foi declarada como "private"
comp3.ligar();

comp1.upRam(-100)

comp1.info();
comp2.info();
comp3.info();