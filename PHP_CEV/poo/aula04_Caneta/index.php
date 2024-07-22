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
            require_once 'Caneta.php';
        
            $c1 = new Caneta("Faber", "Preta", 0.7); //os parâmetros podem ou não ser passados, vai depender do método "construct", vide comentário do arquivo "Caneta.php"
            $c1 -> setModelo("BIC"); //pode ser feito assim tb: $c1->modelo = "BIC";
            $c1 -> setPonta(0.5); // NÃO pode ser feito assim: $c1->ponta = 0.5; porque o atributo 'ponta' não é público, ou seja, so pode ser alterado via 'método'
            print_r($c1);

            print "<hr>Eu tenho uma caneta {$c1->getModelo()} de ponta {$c1->getPonta()}";
            print "<hr>Eu tenho uma caneta ".$c1->getModelo()." de ponta ".$c1->getPonta();
        ?>
    </pre>
    
</body>
</html>