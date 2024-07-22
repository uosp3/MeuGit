<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo</title>
    <link rel="stylesheet" href="../estilos/style.css">
    <?php
        $txt = isset($_GET["t"]) ? $_GET["t"]: "Texto Genérico";
        $tam = isset($_GET["tam"]) ? $_GET["tam"]: "12pt";
        $cor = isset($_GET["cor"]) ? $_GET["cor"]: "#000000";
    ?>
    <style>
        span.texto {
            font-size: <?php echo $tam;?>;
            color: <?php echo $cor;?>;
        }
    </style>
</head>
<body>
    <h1>Assunto: PHP no header</h1>
    <?php
        echo "<p><span class='texto'>$txt</span></p>"
    ?>
    <br>
    <img src="" alt="">
</body>
</html>