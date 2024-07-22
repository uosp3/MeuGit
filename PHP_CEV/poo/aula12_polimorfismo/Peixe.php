<?php
require_once 'Animal.php';
class Peixe extends Animal {
    private $corEscama;
       
    public function alimentar() {
        Print "<p>Comendo susbstâncias</p>";
    }
    public function emitirSom() {
        Print "<p>Peixe não faz som</p>";
    }

    public function locomover() {
        Print "<p>Nadando</p>";
    }

    public function soltarBolha() {
        Print "<p>Soltou uma Bolha</p>";
    }

    public function getCorEscama() {
        return $this->corEscama;
    }

    public function setCorEscama($corEscama) {
        $this->corEscama = $corEscama;
        return $this;
    }
}    