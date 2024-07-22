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
    <h1>Array</h1>
    <pre> <!--faz a exibição do array ficar melhor visualizada-->
        <?php
           $c = range(5, 20, 2); // significa que vai começar em 5, vai até 20 pulando de 2 em 2.
           print_r($c);
           print "<br><hr><br>";

           //FOREACH
           foreach ($c as $v){ //coloca cada elemento do array dentro de $v
            print "$v ";
           }
           print "<br><hr><br>";

           //CHAVES PERSONALIZADAS
           $v = array(3=>5, 1=>9, 0=>8, 7=>7);
           print_r($v);
           $v[] = "E"; //acrescenta um novo valor ao array
           print_r($v);
           print "<br><hr><br>";

           //DESALOCANDO UM VETOR
           unset($v[0]);
           print_r($v);
           print "<br><hr><br>";

           //CHAVES ASSOCIATIVA
           $v =array("nome" => "Ana", "idade" => 23, "peso" => 65.5);
           $v ["fuma"] = true; //acrescentando um novo valor ao array (true=1, false="vazio")
           print_r($v);
           print "<br><hr><br>";

           //FOREACH ASSOCIATIVO
           foreach ($v as $k => $c){
            print "O campo $k possui o conteúdo $c<br>";
           }
           print "<br><hr><br>";

           //MATRIZES EM PHP (array de array)
           $m = array (array(6,4),
                       array(4,9),
                       array(3,2));
            print_r($m);
            print "<br><hr><br>";

            $m[0][1] = $m[2][0]; //troca o 4(linha um[0] coluna 1) pelo 3(linha3[2] coluna zero) no array anterior
            print_r($m);
        ?>
    </pre>
    <br>
    <img src="" alt="">
</body>
</html>