<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Assunto: Operador Unário</h1><br>
    <?php
        $n1 = $_GET["a"];
        $n2 = $_GET["b"];
        $tipo = $_GET["op"];
        echo "Os valors passados foram $n1 e $n2 <br>";
        $r = ($tipo == "s") ? $n1 + $n2 : $n1 * $n2;
        
        echo "<br>O resultado é $r";
    ?>
    <br>
    <img src="imagens/operador_unario.png" alt="">

    <br><h1>Assunto: Igual não é idêntico</h1><br>
    <?php
        $a = 3;
        $b = "3";
        $r = $a == $b ? "iguais" : "identicas"; // IGUAL (==) NÃO É IDÊNTICO (===)
        echo "As variáveis A e B são $r";
    
    ?>
</body>
</html>