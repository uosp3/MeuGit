<?php
require_once 'Controlador.php';
class ControleRemoto implements Controlador {
    //atributos
    private $volume;
    private $ligado;
    private $tocando;
    //metodos especiais
    public function __construct() {
        $this->volume = 50;
        $this->ligado = false;
        $this->tocando = false;
    }    
    private function getVolume() {
        return $this->volume;
    }  
    private function setVolume($volume) {
        $this->volume = $volume;
        return $this;
    }    
    private function getLigado() {
        return $this->ligado;
    }       
    private function setLigado($ligado) {
        $this->ligado = $ligado;
        return $this;
    }    
    private function getTocando() {
        return $this->tocando;
    }    
    private function setTocando($tocando) {
        $this->tocando = $tocando;
        return $this;
    }
    public function ligar() {
        $this->setLigado(true);
    }
    public function desligar() {
        $this->setLigado(false);
    }
    public function abrirMenu() {
        print "<p>---- MENU -----</p>";
        print "<br>Está ligado? ". ($this->getLigado() ? "SIM":"NÃO");
        print "<br>Está tocando: ". ($this->getTocando() ? "SIM":"NÃO");
        print "<br>Volume: ". $this->getVolume();
        for ($i=0; $i <= $this->getVolume(); $i+=10) {
            print "|";
        }
        print "<br>";
    }
    public function fecharMenu() {
        print "<br>Fechando Menu...";
    }
    public function maisVolume() {
        if ($this->getLigado()) {
            $this->setVolume($this->getVolume() + 5);
        }else{
            print "<p>ERRO! Para que o volumme seja alterado é necessário que o aparelho esteja ligado</p>";
        }
    }
    public function menosVolume() {
        if ($this->getLigado()){
            $this->setVolume($this->getVolume() - 5);
        }else{
            print "<p>ERRO! Para que o volumme seja alterado é necessário que o aparelho esteja ligado</p>";
        }
    }
    public function ligaMudo() {
        if ($this->getLigado() && $this->getVolume() > 0){
            $this->setVolume(0);
        }
    }
    public function desligaMudo() {
        if ($this->getLigado() && $this->getVolume()==0) {
            $this->setVolume(50);
        }
    }
    public function play(){
        if ($this->getLigado() && !($this->getTocando())) {
            $this->setTocando(true);
        }
    }
    public function pause() {
        if ($this->getLigado() && $this->getTocando()) {
            $this->setTocando(false);
        }
    }
}