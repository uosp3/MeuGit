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
       include "funcoes.php"; //associa o arquivo funoes.php a este arquivo

     //require "funcoes.php"; ===> tem a mesma funcão que o "include", exceto pelo fato de que caso o arquivo não esteja acessível o escript para de rodar nesse ponto.

     //include_once ou require_once são variações dos comandos acima, vale para o caso de fazer referencia mais de uma vez, ou seja mais de um include ou mais de um require no mesmo aquivo, assim o _once so fará a referencia caso não exista uma anterior.

       print "<h2>Testando novas funções</h2><hr>";
       ola();

       mostraValor(4);
       print "Finalizando programa";
    ?>
    <br>
    <img src="" alt="">
</body>
</html>