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
    <h1>Printf: </h1>
    <?php
        $p = "Leite"; //string - s
        $pr = 4.5; // float - f
        printf ("O %s custa R$ %.2f", $p, $pr);
        //no caso acima o %s representa a variável $p, que é uma string e o
        //%f representa um numero sendo que o .2 é o número de casas decimais formatado.
        // além desse dois casos existe outros, por exemple "%d para decimal e o %u para decimal sem sinal (- e +)
        //o mesmo pode ser feito conforme linha abaixo
        print "<hr>O $p custa R$ " . number_format($pr,2);
    ?>
    <br>
    <img src="" alt="">
</body>
</html>