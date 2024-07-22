"use strict";
//https://www.youtube.com/watch?v=9q7RLxA5yX0
var Veiculos;
(function (Veiculos) {
    class Carro {
        nome;
        motor;
        constructor(nome) {
            this.nome = nome;
            this.motor = new Motores.Motor(100);
        }
    }
    Veiculos.Carro = Carro;
})(Veiculos || (Veiculos = {}));
var Motores;
(function (Motores) {
    class Turbo {
        pot;
        constructor(pot) {
            this.pot = pot;
        }
    }
    class Motor {
        pot;
        constructor(pot) {
            this.pot = pot;
        }
    }
    Motores.Motor = Motor;
})(Motores || (Motores = {}));
const carro1 = new Veiculos.Carro("Rapid");
console.log(carro1.nome);
console.log(carro1.motor);
