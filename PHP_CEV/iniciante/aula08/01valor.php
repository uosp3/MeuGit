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
    <h1>Assunto: Resultado da rais</h1>
    <p>
        <?php
            $valor = $_GET["v"];
            $rq = sqrt($valor);
            echo "A raiz quadrada de $valor é igual a ". number_format($rq,2);
        ?>
    </p>
    <a href="ex01.html">Voltar</a>
    <br>
    <img src="" alt="">
</body>
</html>