<?php

class ContaBanco {
    public $numConta;
    protected $tipo;
    private $dono;
    private $saldo;
    private $status;

    public function __construct() {        
        $this->setSaldo(0);
        $this->setStatus(false); 
        print "<p>Conta criada com sucesso!<p>" ;    
    }

    public function abriConta($t) {
        $this-> setTipo($t);
        $this-> setStatus(true);            
        if ($t=="CC") {                
            $this-> setSaldo(50);
        } elseif ($t=="CP"){
            $this->setSaldo(150);           
        }

    }

    public function fecharConta() {       
        if ($this->getSaldo() > 0) {
            print "Existe um saldo de ". number_format($this->getSaldo(),2)." na conta. Favor sacar para que a conta possa ser fechada<br>";           
          }elseif ($this->getSaldo() < 0){
            print "Existe um saldo negativo de ". number_format($this->getSaldo(),2)." na conta. Favor fazer depósito para que a conta possa ser fechada<br>";
          } else {
            $this->setStatus(false);           
            print "<p>A conta de ". $this->getDono(). " foi encerrada!!<p>";
          }
    }

    public function depositar($v) {       
        if ($this->getStatus()){
            $this->setSaldo($this->getSaldo()+$v);
            print "<p>Depósito de R$ $v na conta de ". $this->getDono()."</p>";
        }else {
            print "Impossível depositar, a conta não está aberta!<br>";
        }
    }

    public function sacar($v) {        
        if ($this->getStatus()){ 
            if($this->getSaldo() >= $v) {
                    $this->setSaldo($this->getSaldo()-$v);
                    print "<p>Saque de R$ $v autorizado na conta de ".$this->getDono(). "</p>";
                }
            else{
                print "Saldo insuficiente para saque!<br>";
            }
        }else{
        print "Impossível sacar, a conta não está aberta!<br>";
        }}

    public function pagarMensal() {
        if ($this->getTipo()=="CC"){
            $v = 12;
        }elseif ($this->getTipo()=="CP"){
            $v = 20;
        }
        if ($this->getStatus()){
            if ($this->getSaldo() > $v){
                $this->setSaldo($this->getSaldo()-$v);
                print "<p>Taxa de serviço mensal de R$ $v debitada na conta de ". $this->getDono()." </p>";
            } else {
                print "Saldo insuficiente!<br>";
            }
        }else{
            print "A conta não está aberta!<br>";
        }
    }

   
    public function setNumConta($numConta) {
        $this->numConta = $numConta;
        return $this;
    }

    
    public function getNumConta() {
        return $this->numConta;
    }

    
    public function setTipo($tipo) {
        $this->tipo = $tipo;
        return $this;
    }

    
    public function getTipo() {
        return $this->tipo;
    }

    
    public function setDono($dono)  {
        $this->dono = $dono;
        return $this;
    }

    
    public function getDono() {
        return $this->dono;
    }

    
    public function setSaldo($saldo) {
        $this->saldo = $saldo;
        return $this;
    }

    
    public function getSaldo() {
        return $this->saldo;
    }

    
    public function setStatus($status) {
        $this->status = $status;
        return $this;
    }

    public function getStatus() {
        return $this->status;
    }
}
