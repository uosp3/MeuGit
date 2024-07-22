<?php
require_once 'Pessoa.php';
class Aluno extends Pessoa {
    private $mat;
    private $curso;

    public function cancelarMatr() {
        print "<p>Matrícula será cancelada</p>";
    }

    public function getMat() {
        return $this->mat;
    }

    public function setMat($mat) {
        $this->mat = $mat;
        return $this;
    }

    public function getCurso() {
        return $this->curso;
    }

    public function setCurso($curso) {
        $this->curso = $curso;
        return $this;
    }
}