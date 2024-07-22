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
    <h1>Estados e regiões</h1>
    <?php
       $regiao = $_GET['regiao'];
       
           switch ($regiao){
                case 1:
                    echo "<p>Você mora na regiao Sudeste</p>";
                    break;
                case 2:
                    echo "<p>Você mora na regiao Sul</p>";
                    break;
                case 3:
                    echo "<p>Você mora na regiao Nordeste</p>";
                    break;
                case 4:
                    echo "<p>Você mora na regiao Centro Oeste</p>";
                    break;
                case 5:
                    echo "<p>Você mora na regiao Norte</p>";
                    break;
                default:
                    echo "<p>Voce não selecionou nenhum estado...</p>";
           }    
    ?>
    <br>
    <img src="" alt="">
</body>
</html>