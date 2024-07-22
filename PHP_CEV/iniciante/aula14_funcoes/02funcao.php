<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Funções</h1>
    <?php
        function soma ($a, $b){
            $s = $a + $b;
            return $s; //aqui, no lugar de $s pode ser colocado $a + $b e excluir a linha acima.
            
            // no lugar da linha acima poderia ser: print $s (assim seria uma função que não retorna valor, um procedimento.)
        }
        $x = 3;
        $y = -4;
        $r = soma($x, $y);
        print "A soma entre $x e $y é igual a $r";
    ?>
    <br>
    <img src="" alt="">
</body>
</html>