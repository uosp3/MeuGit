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
    <h1>Passagem de parâmetros: </h1>
    
    <?php
        function teste ($x){ // passagem de parâmetro por valor
            $x = $x + 2;
            print "<p>O valor de X é $x</p>";
        }

        $a = 3;
        teste($a);
        print "<p>O valor de A é $a</p><br><hr><br>";

        // as funções divergem apenas no & que é acrescentado na função abaixo

        function teste2 (&$x){ // passagem de parâmetro por referencia, vide &
            $x = $x + 2;
            print "<p>O valor de X é $x</p>";
        }

        $a = 3;
        teste2($a);
        print "<p>O valor de A é $a</p>"
    ?>
    <br>
    <img src="" alt="">
</body>
</html>