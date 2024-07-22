"use strict";
class Conta {
    //https://www.youtube.com/watch?v=Q73LywpCSLk
    //https://www.youtube.com/watch?v=Q73LywpCSLk&list=PLx4x_zx8csUhtPMrkiGvFJVE5LX8Qat5s&index=26
    numero; //readonly não permite alteração do nr da conta
    titular;
    saldoconta;
    constructor(titular) {
        this.numero = this.gerarNumeroConta();
        this.titular = titular;
        this.saldoconta = 0;
    }
    gerarNumeroConta() {
        return Math.floor(Math.random() * 100000) + 1;
    }
    info() {
        console.log(`Titular: ${this.titular}`);
        console.log(`Número: ${this.numero}`);
    }
    get saldo() {
        return this.saldoconta;
    }
    set saldo(saldoconta) {
        this.saldoconta = saldoconta;
    }
    deposito(valor) {
        if (valor < 0) {
            console.log(`Valor inválido`);
            return;
        }
        this.saldo += valor;
    }
    saque(valor) {
        if (valor < 0) {
            console.log(`Valor inválido`);
            return;
        }
        if (valor <= this.saldoconta) {
            this.saldo -= valor;
        }
        else {
            console.log(`Saldo insuficionete`);
        }
    }
}
class ContaPF extends Conta {
    taxaCalculo = 10; //**
    cpf;
    constructor(cpf, titular) {
        super(titular);
        this.cpf = cpf;
    }
    CalcularTrib(valor) {
        return valor * this.taxaCalculo;
    }
    info() {
        console.log(`Tipo...:PF`);
        super.info();
        console.log(`CPF....: ${this.cpf}`);
        console.log(`---------------------`);
    }
    deposito(valor) {
        if (valor > 1000) {
            console.log(`Valor de depósito muito grande para este tipo de conta`);
        }
        else {
            super.deposito(valor);
        }
    }
    saque(valor) {
        if (valor > 1000) {
            console.log(`Valor de saque muito grande para este tipo de conta`);
        }
        else {
            super.saque(valor);
        }
    }
}
class ContaPJ extends Conta {
    cnpj;
    constructor(cnpj, titular) {
        super(titular);
        this.cnpj = cnpj;
    }
    info() {
        console.log(`Tipo...:PJ`);
        super.info();
        console.log(`CNPJ...: ${this.cnpj}`);
        console.log(`---------------------`);
    }
    deposito(valor) {
        if (valor > 10000) {
            console.log(`Valor de depósito muito grande para este tipo de conta`);
        }
        else {
            super.deposito(valor);
        }
    }
    saque(valor) {
        if (valor > 10000) {
            console.log(`Valor de saque muito grande para este tipo de conta`);
        }
        else {
            super.saque(valor);
        }
    }
}
const cont1 = new ContaPF(111, "Edson");
const cont2 = new ContaPJ(222333, "Gomes");
//console.log(cont1.titular)
//console.log(cont1.numero)
cont1.deposito(800);
cont1.deposito(200);
cont1.deposito(1000);
//cont1.saque(1000)
//cont1.saque(500)
//cont1.saque(500)
//cont1.saque(10)
console.log(cont1.saldo);
// cont2.deposito(10000)
// cont2.deposito(10000)
// cont2.deposito(10000)
// cont2.deposito(10000)
// console.log(cont2.saldo())
cont1.info();
//cont2.info()
