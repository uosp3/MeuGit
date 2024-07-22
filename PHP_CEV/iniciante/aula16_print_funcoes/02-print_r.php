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
    <h1>Print_r: Vetores </h1>
    <pre>
        <?php
           $v[0] = 4;
           $v[1] = 8;
           $v[2] = 3;
           print_r($v);// mostra os array e seus índices
           print "<br>O vetor tem ".count($v). " elementos"; //conta os elementos do array
           print "<hr><hr>";
           $v2 = array(3, 7, 6, "teste", 1, 9);
           print_r($v2);
           print "<hr><hr>";
        
           var_dump($v2);//mostra o total de arrays e seus índices e o tipo da variável
           print "<hr><hr>";
        
           var_export($v)// tb mostra os array e seu índices, com uma formatação diferente.
        ?>
    </pre>
    <br>
    <img src="" alt="">
</body>
</html>