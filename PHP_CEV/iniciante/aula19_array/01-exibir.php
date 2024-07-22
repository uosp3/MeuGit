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
    <h1>Array, acréscimo e decréscimo </h1>
    <pre>
        <?php
            $v = array("a", "j", 10, "m", "x", "k");
            print_r($v);
            print "<br><hr>";
            array_push($v, "t"); //acrescenta um elemento ao final do array
            print_r($v);
            print "<br><hr>";
            array_pop($v); //elimina o último elemento do array
            print_r($v);
            print "<br><hr>";
            array_unshift($v, "t"); //acrescenta um elemento no início do array
            print_r($v);
            print "<br><hr>";
            array_shift($v); //elimina o primeiro elemento do array
            print_r($v);
            print "<br><hr>";

            sort($v); //ordena os elementos do array crescente 
            print_r($v);
            print "<br><hr>";

            rsort($v); //ordena os elementos do array decrescente 
            print_r($v);
            print "<br><hr>";

            asort($v); //ordena os elementos do array crescente SEM ALTERAR O INDICE
            print_r($v);
            print "<br><hr>";

            arsort($v); //ordena os elementos do array decrescente SEM ALTERAR O ÍNDICE
            print_r($v);
            print "<br><hr>";

            $v = array(2=>"a", 5=>"j", 0=>10, 3=>"m", 4=>"x", 1=>"k");
            print_r($v);
            ksort($v); //ordena os indices do array crescente 
            print_r($v);
            print "<br><hr>";

            $v = array(2=>"a", 5=>"j", 0=>10, 3=>"m", 4=>"x", 1=>"k");
            print_r($v);
            krsort($v); //ordena os indices do array DEcrescente 
            print_r($v);




        ?>
    </pre>
    <br>
    <img src="" alt="">
</body>
</html>