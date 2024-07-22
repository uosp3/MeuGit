<?php
abstract class Pessoa { //classe abstrata não pode ser instanciada
    protected $nome;
    protected $idade;
    protected $sexo;

    public final function fazerAniversario() { //'final' indica que o metodo não pode ser sobreposto
        $this->idade ++;
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
}

