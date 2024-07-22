<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo</title>
    <style>
       

    </style>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Operadores lógicos</h1>
    <p>
        <?php
            $ano = $_GET["an"];
            $idade = date('Y') - $ano;
            echo "Quem nasceu em $ano tem $idade anos de idade.";
            $tipo = ($idade >=18 && $idade <65) ? "é obrigatório" : "Não é obrigatório";
            echo "<br>Com essa idade seu voto $tipo"
        ?>
    </p>
    <br>
    <div><img src="imagens/operadores_logicos.png" alt="figura"></div>
</body>
</html>