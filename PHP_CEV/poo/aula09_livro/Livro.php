<?php
require_once 'Pessoa.php';
require_once 'Publicacao.php';
class Livro implements Publicacao {
    //atributos
    private $titulo;
    private $autor;
    private $totPaginas;
    private $pagAtual;
    private $aberto;
    private $leitor;
    //metodo
    public function detalhes() {
        print "<hr>Livro ". $this->titulo. " escrito por ". $this->autor;
        print "<br>Páginas: ". $this->totPaginas. ". atual ". $this->pagAtual;
        print "<br> Sendo lido por ". $this->leitor->getNome()."<br>";
    }
    //metodos especiais
    public function __construct($titulo, $autor, $totPaginas, $leitor) {
        $this->titulo = $titulo;
        $this->autor = $autor;
        $this->totPaginas = $totPaginas; 
        $this->aberto = false;
        $this->pagAtual = 0;
        $this->leitor = $leitor;      
    }
    
    public function getTitulo() {
        return $this->titulo;
    }

    public function setTitulo($titulo) {
        $this->titulo = $titulo;
        return $this;
    }

    public function getAutor() {
        return $this->autor;
    }

    public function setAutor($autor) {
        $this->autor = $autor;
        return $this;
    }
 
    public function getTotPaginas() {
        return $this->totPaginas;
    }

    public function setTotPaginas($totPaginas) {
        $this->totPaginas = $totPaginas;
        return $this;
    }

    public function getPagAtual() {
        return $this->pagAtual;
    }

    public function setPagAtual($pagAtual) {
        $this->pagAtual = $pagAtual;
        return $this;
    }

    public function getAberto() {
        return $this->aberto;
    }

    public function setAberto($aberto) {
        $this->aberto = $aberto;
        return $this;
    }

    public function getLeitor() {
        return $this->leitor;
    }

    public function setLeitor($leitor) {
        $this->leitor = $leitor;
        return $this;
    }

    public function abrir() {
        $this->aberto = true;
    }
    public function fechar() {
        $this->aberto = false;
    }
    public function folhear($p) {
        if ($p > $this->totPaginas) {
           $this->pagAtual=0;
        } else {
            $this->pagAtual = $p;
        }
    }
    public function avancarPag() {
        if ($this->getPagAtual() !=$this->getTotPaginas()) {
            $this->pagAtual++;
        } else {
            $this->aberto = false;
            $this->pagAtual = 0;
            print "<br> Você ja estava na última página, o livro foi fechado!";
        }
        
    }
    public function voltarPag() {
        if ($this->getPagAtual() == 1){
            $this->pagAtual--;
            $this->aberto = false;
            print "<br> Voce fechou o livro";
        } else {
        $this->pagAtual--;
        }
    }
}
