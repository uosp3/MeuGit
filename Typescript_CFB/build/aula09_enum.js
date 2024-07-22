"use strict";
var dias;
(function (dias) {
    dias[dias["domingo"] = 0] = "domingo";
    dias[dias["segunda"] = 1] = "segunda";
    dias[dias["terca"] = 2] = "terca";
    dias[dias["quarta"] = 3] = "quarta";
    dias[dias["quinta"] = 4] = "quinta";
    dias[dias["sexta"] = 5] = "sexta";
    dias[dias["sabado"] = 6] = "sabado";
})(dias || (dias = {}));
console.log(dias.domingo); //ou
console.log(dias['domingo']); //assim retorna o valor que está associado à chave
console.log(dias[1]); //assim retorna o nome da chave
const d = new Date();
console.log(d); //retorna data completa com hora
console.log(d.getDate()); //retorna o dia do mes
console.log(d.getDay()); //retorna o dia da samana (em número)
console.log(dias[d.getDay()]); //retorna o dia da samana (em texto)
var cores;
(function (cores) {
    cores["branco"] = "#fff";
    cores["preto"] = "#000";
    cores["vermelho"] = "f00";
    cores["verde"] = "#0f0";
    cores["azul"] = "#00f";
})(cores || (cores = {}));
console.log(cores.branco);
console.log(cores['branco']);
var tipoUsuario;
(function (tipoUsuario) {
    tipoUsuario[tipoUsuario["USER"] = 10] = "USER";
    tipoUsuario[tipoUsuario["ADMIN"] = 100] = "ADMIN";
    tipoUsuario[tipoUsuario["SUPER"] = 1000] = "SUPER";
})(tipoUsuario || (tipoUsuario = {}));
const tp = tipoUsuario.SUPER;
console.log(tp);
