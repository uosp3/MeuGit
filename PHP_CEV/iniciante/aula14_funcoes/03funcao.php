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
    <h1>Função de múltiplos parâmetros</h1>
    <?php
        function soma(){
            $p = func_get_args();// cria um array
            $t = func_num_args();// conta os itens passados
            $s = 0;
            for ($i=0; $i<$t; $i++){
                $s = $s + $p[$i];              
            }
            return $s;
        }
        $r = soma(3,5,2); // pode ser acrescentado quantos parâmetros quiser que a função vai funcionar.
        print "A soma dos valores é $r";
    ?>
    <br>
    <img src="" alt="">
</body>
</html>