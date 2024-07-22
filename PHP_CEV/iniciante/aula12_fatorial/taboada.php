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
    <?php
        $multiplicando = $_GET["numero"];  
        echo "<h1>Taboada de $multiplicando</h1>";      
        echo "<p>Mostrando a taboada de $multiplicando</p>";
        "<div>";
        echo "01 X $multiplicando = $multiplicando<br>";
        $multiplicador = 2;
        while ($multiplicador <= 9){
            echo "0$multiplicador X $multiplicando = ".($multiplicador*$multiplicando)."<br>";
            $multiplicador++;
        }
        echo $multiplicador." X ". $multiplicando." = ".($multiplicador*$multiplicando);
        "</div>";
    ?>
    <br>
    <img src="" alt="">
</body>
</html>