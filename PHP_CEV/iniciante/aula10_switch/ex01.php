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
    <h1>Assunto: Switch </h1>
    <?php
        $n = isset($_GET["num"]) ? $_GET["num"] : 0;
        $o = isset($_GET["oper"]) ? $_GET["oper"] : 1;

        switch ($o){
            case 1:
                $r = $n * 2;
                break;
            case 2:
                $r = $n**3; // ou $r = pow($n,3);
                break;
            case 3:
                $r = sqrt($n);
        }
        echo "O Resultado da operação solicitada é ". round($r,2)
    ?>
    <br>
    <img src="" alt="">
</body>
</html>