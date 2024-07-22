<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../estilos/style.css">
    <title>Valores passados pela url</title>
</head>
<body>
    <h1>Valores passados pela url</h1>
    <?php
    // exemplo http://127.0.0.1/PHP/aula05/operadores.php?a=5&b=7
    $n1 = $_GET["a"];
    $n2 = $_GET["b"];
    echo "<h2>Valores recebidos: $n1 e $n2</h1><br>"    
    ?>
    <img src="imagens/operadores2.png" alt="operadores2">
</body>
</html>