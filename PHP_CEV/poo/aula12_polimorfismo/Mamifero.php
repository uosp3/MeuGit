<?php
require_once 'Animal.php';
class Mamifero extends Animal {
    private $corPelo;
       
    public function alimentar() {
        Print "<p>Mamando</p>";
    }
    public function emitirSom() {
        Print "<p>Som de Mamífero</p>";
    }

    public function locomover() {
        Print "<p>Correndo</p>";
    }

    public function getCorPelo() {
        return $this->corPelo;
    }

    public function setCorPelo($corPelo) {
        $this->corPelo = $corPelo;
        return $this;
    }
}    