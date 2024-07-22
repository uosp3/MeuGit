//string, boolean, number
let x: number = 10;

x = 12;

console.log(x);

//inferencia x annotation
let y = 12; // inferencia, não foi declarado tipo
let z:number = 12; //annotation, o tipo foi explicitado



// tipos básicos
let firstName: string = "Edson";
let age: number = 61;
const isAdmin: boolean = true;
const myNumbers: number[] = [1,2,3];

//myNumbers.toUpperCase(); // não existe maiúlculas para mumeros
firstName.toUpperCase(); // para string é aceito

//tuplas
let myTuple: [number, string, string[]]
myTuple =[5, 'teste', ['a','b']]// as atribuições tem que seguir o que foi predefinido.

//object literals -> {prop: value}
const user: {name:string; age:number} = {
    name: 'Edson',
    age: 61,
}

//any -> faz com que a variável aceite qualquer tido (não é recomendável usar)
let a: any = 0;
a = "teste";
a = true;
a = [];

// union type -> é uma alternativa ao any.
let id: string | number = '10';
id = 20;
//id = true; // não será aceito pois não foi definido como boolean


//type alias -> cria uma regra para ser usada com uma função, para não ter que ficar repetindo o tipo
type myIdType = number | string
const userId: myIdType = "Gomes";
const productId: myIdType = 1025;

//enum
// tamanho de roupas (size: Médio, size: Pequeno)
enum Size{
    P= "Pequeno",
    M= "Médio",
    G= "Grande",
}
const camisa = {
    nome: "Camisa gola V",
    size: Size.G,
}
console.log(camisa)