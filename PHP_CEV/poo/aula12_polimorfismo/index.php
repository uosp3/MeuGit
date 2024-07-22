<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <pre>
        <?php
            require_once 'Mamifero.php';
            require_once 'Reptil.php';
            require_once 'Peixe.php';
            require_once 'Ave.php';
            require_once 'Canguru.php';
            require_once 'Cachorro.php';
            require_once 'Tartaruga.php';

            $m = new Mamifero();
            $a = new Ave();
            $r = new Reptil();
            $c = new Canguru();
            $k = new Cachorro();
            $t = new Tartaruga();

            //polimorfismo: os metodos abaixo são os mesmo mas de classe diferentes, portanto retoram informações específicas de cada um. Um sobrepoe ao outro.
            $m->locomover();
            $a->locomover();
            $r->locomover();
            $c->locomover();
            $k->emitirSom();
            $t->locomover();
            
            print "<p>Vide foto na pasta imagens</p>";
        ?>
    </pre>
</body>
</html>