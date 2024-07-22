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
    <h1>Desafio: Incremento e decremento <br> While</h1> 
    <?php
        $i = $_GET["inicio"];
        $f = $_GET["final"];
        $c = $_GET["incremento"];
        $d = $i;
        echo "Inicio $i<br> Final $f<br> Incremento $c<br>";

        while ($i <= $f) {            
            echo $i."&nbsp&nbsp&nbsp&nbsp&nbsp";
            $i = $i + $c;
        }

        while ($d >= $f) {
            echo $d."&nbsp&nbsp&nbsp&nbsp&nbsp";
            $d = $d - $c;
        }

    ?>
    <br>
    <img src="" alt="">
</body>
</html>