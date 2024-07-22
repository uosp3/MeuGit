<?php
class Caneta {
    private $modelo;
    private $cor;
    private $ponta;
    private $tampada;

    /*
    public function __construct() { 
        $this->cor = "Aul";
        $this->tampar();
    }
    */

    /*as linhas abaixo tb podem ser usadas para a construção do objeto, neste caso ja são passados os parâmetros.*/

    public function __construct($m, $c, $p) {
        $this->modelo = $m;
        $this->cor = $c;
        $this->ponta = $p;
        $this->tampar();
    }


    public function tampar() {
        $this->tampada = true;
    }

    public function getModelo() {
        return $this->modelo;
    }

    public function setModelo($m) {
        $this->modelo = $m;
    }

    public function getPonta() {
        return $this->ponta;
    }

    public function setPonta($p) {
        $this->ponta = $p;
    }
    
}
