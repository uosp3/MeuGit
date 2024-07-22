<?php
require_once 'Animal.php';
class Ave extends Animal {
    private $corPena;
       
    public function alimentar() {
        Print "<p>Comendo Frutas</p>";
    }
    public function emitirSom() {
        Print "<p>Som de ave</p>";
    }

    public function locomover() {
        Print "<p>Voando</p>";
    }

    public function fazerNinho() {
        Print "<p>Construindo um ninho</p>";
    }
       
    public function getCorPena() {
        return $this->corPena;
    }

    public function setCorPena($corPena) {
        $this->corPena = $corPena;
        return $this;
    }
    }