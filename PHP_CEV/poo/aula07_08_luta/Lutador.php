<?php
class Lutador {
    //Atributos
    private $nome;
    private $nacionalidade;
    private $idade, $altura, $peso;
    private $categoria, $vitorias, $derrotas, $empates;
    //Métodos
    function apresentar() {
        print "<p>----------------------------</p>";
        print "<p>CHEGOU A HORA! O lutador " . $this->getNome();
        print " veio diretamente de " . $this->getNacionalidade();
        print " tem " . $this->getIdade() ." anos e pesa " . $this->getPeso() ."kg";
        print "<br>Ele tem " . $this->getVitorias() . " vitórias ";
        print $this->getDerrotas() . " derrotas e " . $this->getEmpates() . " empates</p>";
    }
    function status() {
        print "<p>----------------------------</p>";
        print "<p>". $this->getNome(). " é um peso ". $this->getCategoria();
        print ", tem ". $this->getVitorias() . " vitória(s) ";
        print ", tem ". $this->getDerrotas() . " derrota(s) e ". $this->getEmpates(). " empate(s)!</p>";
    }
    function ganharLuta() {
        $this->setVitorias($this->getVitorias() + 1);
    }
    function perderLuta() {
        $this->setDerrotas($this->getDerrotas() + 1);
    }
    function empatarLuta() {
        $this->setEmpates($this->getEmpates() + 1);
    }
    //Métodos Especiais
    function __construct($no, $na, $id, $al, $pe, $vi, $de, $em) {
        $this->nome = $no;
        $this->nacionalidade = $na;
        $this->idade = $id;
        $this->altura = $al;
        $this->setPeso($pe);
        $this->vitorias = $vi;
        $this->derrotas = $de;
        $this->empates = $em;
    }

    
    public function getNome() {
        return $this->nome;
    }

    
    public function setNome($nome) {
        $this->nome = $nome;
        return $this;
    }

   
    public function getNacionalidade() {
        return $this->nacionalidade;
    }

    
    public function setNacionalidade($nacionalidade) {
        $this->nacionalidade = $nacionalidade;
        return $this;
    }

   
    public function getIdade() {
        return $this->idade;
    }

    
    public function setIdade($idade) {
        $this->idade = $idade;
        return $this;
    }

    
    public function getAltura() {
        return $this->altura;
    }

    
    public function setAltura($altura) {
        $this->altura = $altura;
        return $this;
    }

    
    public function getPeso() {
        return $this->peso;
    }

   
    public function setPeso($peso) {
        $this->peso = $peso;
        $this->setCategoria();
        return $this;
    }

   
    public function getCategoria() {
        return $this->categoria;
    }

    
    private function setCategoria() {
       if ($this->peso <52.2) {
        $this->categoria = "Inválido";
       } elseif ($this->peso <=70.3) {
        $this->categoria = "Leve";
       } elseif ($this->peso <=83.9) {
        $this->categoria = "Médio";
       } elseif ($this->peso <=120.2) {
        $this->categoria = "Pesado";
       }else {
        $this->categoria = "Inválido";
       }
    }

    
    public function getVitorias() {
        return $this->vitorias;
    }

    
    public function setVitorias($vitorias) {
        $this->vitorias = $vitorias;
        return $this;
    }

    
    public function getDerrotas() {
        return $this->derrotas;
    }

    
    public function setDerrotas($derrotas) {
        $this->derrotas = $derrotas;
        return $this;
    }

    
    public function getEmpates() {
        return $this->empates;
    }

    
    public function setEmpates($empates) {
        $this->empates = $empates;
        return $this;
    }
}
