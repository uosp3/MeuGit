<?php
require_once 'Lutador.php';
class Luta {
    //atributos
    private $desafiado;
    private $desafiante;
    private $rounds;
    private $aprovada;
    //métodos públicos
    public function marcarLuta($l1, $l2) {
        if ($l1->getCategoria() === $l2->getCategoria() && ($l1 != $l2)) {
            $this->aprovada = true;
            $this->desafiado = $l1;
            $this->desafiante = $l2;
        }else{
            $this->aprovada = false;
            $this->desafiado = null;
            $this->desafiante = null;
        }
    }
    public function lutar() {
        if ($this->aprovada) {
            $this->desafiado->apresentar();
            $this->desafiante->apresentar();
            $vencedor = rand(0 , 2);//numero aleatório entre 0 e 2
            switch($vencedor) {
                case 0: // empate
                    print "<p>Empate!</p>";
                    $this->desafiado->empatarLuta();
                    $this->desafiante->empatarLuta();
                    break;
                case 1: // desafiado vence
                    print "<p>".$this->desafiado->getNome()." venceu!</p>";
                    $this->desafiado->ganharLuta();
                    $this->desafiante->perderLuta();
                    break;
                case 2: //desafiante vence
                    print "<p>".$this->desafiante->getNome()." venceu!</p>";
                    $this->desafiante->ganharLuta();
                    $this->desafiado->perderLuta();
                    break;
            }
        } else {
            print "<p>Luta não pode acontecer</p>";
        }
    }
    //métodos especiais   
    public function getDesafiado() {
        return $this->desafiado;
    }

    public function setDesafiado($desafiado) {
        $this->desafiado = $desafiado;
        return $this;
    }

    public function getDesafiante() {
        return $this->desafiante;
    }
    
    public function setDesafiante($desafiante) {
        $this->desafiante = $desafiante;
        return $this;
    }

    public function getRounds() {
        return $this->rounds;
    }

    public function setRounds($rounds) {
        $this->rounds = $rounds;
        return $this;
    }

    public function getAprovada() {
        return $this->aprovada;
    }

    public function setAprovada($aprovada) {
        $this->aprovada = $aprovada;
        return $this;
    }

    
}