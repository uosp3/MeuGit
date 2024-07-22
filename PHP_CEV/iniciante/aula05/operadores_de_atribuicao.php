<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Operadores de atribuição</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Operadores de atribuição.</h1>
    <br>
    <?php
        $preco = $_GET["p"];
        echo "O preço do produto é R$ ". number_format($preco, 2, ".", ".");
        $juros = .1;
        $preco -= $preco*$juros;        
        echo "<br>E o novo preço com " .($juros*100). "% de desconto é R$ ". number_format($preco,2,",",".");    
    ?>
    <br><br>
    <img src="imagens/operadores3.png" alt="atribuicoes">    
</html>