enum dias{ // a numeração abaixo é facultativa se quiser que fique em sequencia.
    domingo=0,
    segunda=1,
    terca=2,
    quarta=3,
    quinta=4,
    sexta=5,
    sabado=6
}
console.log(dias.domingo) //ou
console.log(dias['domingo']) //assim retorna o valor que está associado à chave
console.log(dias[1])//assim retorna o nome da chave

const d=new Date();
console.log(d)//retorna data completa com hora
console.log(d.getDate())//retorna o dia do mes
console.log(d.getDay())//retorna o dia da samana (em número)
console.log(dias[d.getDay()])//retorna o dia da samana (em texto)

enum cores{
    branco="#fff",
    preto="#000",
    vermelho="f00",
    verde="#0f0",
    azul="#00f"
}
console.log(cores.branco);
console.log(cores['branco']);

enum tipoUsuario{
    USER=10,
    ADMIN=100,
    SUPER=1000
}

const tp:tipoUsuario=tipoUsuario.SUPER;
console.log(tp)