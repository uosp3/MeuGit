<?php
 abstract class Pessoa {
    //atributos
     protected $nome;
     protected $idade;
     protected $sexo;
     protected $experiencia;

     public function __construct($nome, $idade, $sexo) {
        $this->nome = $nome;
        $this->idade = $idade;
        $this->sexo = $sexo;
        $this->experiencia = 0;
     }

     private function ganharExp($n){
        $this->experiencia += $n;
     }

     public function getNome() {
          return $this->nome;
     }

     public function setNome($nome) {
          $this->nome = $nome;
          return $this;
     }
 
     public function getIdade() {
          return $this->idade;
     }

     public function setIdade($idade) {
          $this->idade = $idade;
          return $this;
     }

     public function getSexo() {
          return $this->sexo;
     }

     public function setSexo($sexo) {
          $this->sexo = $sexo;
          return $this;
     }

     public function getExperiencia() {
          return $this->experiencia;
     }

     public function setExperiencia($experiencia) {
          $this->experiencia = $experiencia;
          return $this;
     }
}