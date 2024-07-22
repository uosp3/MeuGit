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
    <h1>Assunto: Pegando dados do formulário</h1>
    <?php
    // a linha abaixo é uma solução paleativa caso não receba valor pela url
        $nome = isset($_GET["nome"]) ? $_GET["nome"] :"[não informado]";
        $ano = $_GET["ano"];
        $sexo = $_GET["sexo"];
        $idade = date("Y") - $ano;
        echo "$nome é $sexo e tem $idade anos.";
    ?>
    <br>
    <img src="" alt="">
    <a href="ex02.html">Voltar</a>
</body>
</html>