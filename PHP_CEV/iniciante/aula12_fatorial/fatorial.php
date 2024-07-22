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
    <h1>Fatorial </h1>
    <?php
    // não fiz a página anterior, passar o parâmetro "val" atravéz da url
        $v = $_GET["val"];
        echo "<p>Calculando o fatoria de $v</p>";
        $c = $v;
        $fat = 1;
        do {
            $fat = $fat * $c;
            echo $fat."<br>";
            $c--;
        } while ($c >= 0);
        
        if ($fat <> 0) {
            echo "<p>$v! = $fat</p>";
        } else {
            echo "<p>$v! = 1</p>";
        }

    ?>
    <br>
    <img src="" alt="">
</body>
</html>