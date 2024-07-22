<?php
interface Controlador {
    public function ligar();
    public function desligar();
    public function abrirMenu();
    public function fecharMenu();
    public function maisVolume();
    public function menosVolume();
    public function ligaMudo();
    public function desligaMudo();
    public function play();
    public function pause();
    
}