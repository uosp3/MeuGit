<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 02 - POO</title>
</head>
<body>
    
        <?php
           require_once 'Caneta.php'; // carrega o arquivo
            $c1 = new Caneta;
            $c1->cor = "Azul";
            $c1->ponta = 0.5;
            $c1->tampada = false;

            $c1->destampar();

            $c1->rabiscar();

            print "<pre>";
            print_r($c1);
            print "</pre>";
        ?>
    
</body>
</html>