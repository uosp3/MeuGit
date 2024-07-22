let coisas:[string,number,boolean]=["Corda", 10, true] //define quais tipos de dados e sua ordem.
coisas.push("Kit médico", 5, true) //o código aceita a instrução mas não efetiva a inclusão dos dados pois, inicialmente, o array foi definido com apenas 3 elementos. Para evitar isso bastar definir o array como readonly
coisas[2]=false;//altera o conteúdo do índice 2

console.log(coisas);
console.log(coisas[2]);//imprime so o índice 2.