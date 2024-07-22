<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funcões Aritméticas</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Funcões Aritméticas</h1>
    <?php
        $v1 = $_GET["x"];
        $v2 = $_GET["y"];
        echo "<h2>Valores recebidos: $v1 e $v2</h2>";
        echo "O valor absoluto de $v2 é ". abs($v2);
        echo "<br><br>O valor de $v1<sup>$v2</sup> é ". pow($v1, $v2);
        echo "<br>A raiz de $v1 é ". sqrt($v1);
        echo "<br>O valor de $v2 arredondado é ". round($v2);// ceil = arredonda pra cima e floor = arredonda pra baixo
        echo "<br>A parte inteir e $v2 é ". intval($v2);
        echo "<br>O valor de $v1 em moeda é R$". number_format($v1,2,",", ".");// 2 é o numero de casas decimais e a "vírgula" é o tipo do separador e o "ponto" é o separador de milhar
    ?>
    <br>
    <img src="imagens/funcoesmatematicas.png" alt="funcoes">    
</body>
</html>