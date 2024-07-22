<?php
require_once 'Animal.php';
class Reptil extends Animal {
    private $corEscama;

    public function alimentar() {
        Print "<p>Comendo Vegetais</p>";
    }
    public function emitirSom() {
        Print "<p>Som de Reptil</p>";
    }

    public function locomover() {
        Print "<p>Rastejando</p>";
    }
    
    public function getCorEscama() {
        return $this->corEscama;
    }

    public function setCorEscama($corEscama) {
        $this->corEscama = $corEscama;
        return $this;
    }
}