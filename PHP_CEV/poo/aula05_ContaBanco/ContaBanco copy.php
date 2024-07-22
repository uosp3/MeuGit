<?php

class ContaBanco {
    public $numConta;
    protected $tipo;
    private $dono;
    private $saldo;
    private $status;

    public function __construct() {        
        $this->saldo = 0;
        $this->status = false;      
    }

    public function abriConta($tipo) {
        $this-> setTipo($tipo);
        $this-> setStatus(true);            
        if ($tipo=="CC") {                
            $this-> setSaldo(50);
        } elseif ($tipo=="CP"){
            $this->setSaldo(150);           
        }

    }

    public function fecharConta() {
        $saldo = $this->getSaldo()-150;
        if ($saldo > 0) {
            print "Existe um saldo de ". number_format($saldo,2)." na conta. Favor sacar para que a conta possa ser fechada<br>";           
          }elseif ($saldo < 0){
            print "Existe um saldo negativo de ". number_format($saldo,2)." na conta. Favor fazer depósito para que a conta possa ser fechada<br>";
          } else {
            $this->setStatus(false);
            $this->setSaldo(0);// apenas para teste, deletar depois
            print "A conta foi encerrada!!<br>";
          }
    }

    public function depositar($dep) {
        $status = $this->getStatus();
        if ($status==1){
            $this->setSaldo($this->getSaldo()+$dep);
        }else {
            print "Impossível depositar, a conta não está aberta!<br>";
        }
    }

    public function sacar($sac) {
        $status = $this->getStatus();
        if ($status==1){ 
            if($this->getSaldo() > $sac) {
                    $this->setSaldo($this->getSaldo()-$sac);
                }
            else{
                print "Saldo insuficiente!<br>";
            }
        }else{
        print "Impossível sacar, a conta não está aberta!<br>";
        }}

    public function pagarMensal() {
        if ($this->getTipo()=="CC"){
            $tx = 12;
        }elseif ($this->getTipo()=="CP"){
            $tx = 20;
        }
        if ($this->getStatus()==1){
            if ($this->getSaldo() > $tx){
                $this->setSaldo($this->getSaldo()-$tx);
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
