<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aprendendo PHP</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Incrementos</h1><br>
    <?php
        $atual = $_GET["aa"];
        echo "O ano atual é $atual e o ano anterior foi ". --$atual;
    ?>
    <br><br>
    <img src="imagens/incremento.png" alt="incremento">
    
</body>
</body>
</html>