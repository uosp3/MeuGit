<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo</title>
    <link rel="stylesheet" href="../estilos/style.css">
    <style>
        p {
            font-size: 35px;
        }
    </style>
</head>
<body>
    <h1>Assunto: Média escolar</h1>
    <p>
        <?php
            $n1 = $_GET["n1"];
            $n2 = $_GET["n2"];
            $m = ($n2 + $n1)/2;
            echo "A média entre $n1 e $n2 é gual a $m <br>";
            if ($m < 5){
                 $sit = "Reprovado";
                } elseif ($m >=5 && $m < 7){
                        $sit = "Em recuperação";
                    } else {
                        $sit = "Aprovado";
                    }

            echo "Situação do aluno: $sit";
        ?>
    </p>
    <br>
    <img src="" alt="">
</body>
</html>