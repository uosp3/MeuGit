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
    <h1>Criando conteúdos dinâmicamente : </h1>
    <?php
    $i = 1; //1º while pega os dados da url
    while($i<=5){
        $v = "num".$i;
        $url = "v".$i;
        $$v = isset($_GET[$url])?$_GET[$url]:0;
        $i++;
    }
        /*echo "$num1 $num2 $num3 $num4 $num5"; //assim fica inline*/

    $i=1; //este bloco mostra os dados pegos pela url
    while($i<=5){
        $v = "num".$i;
        echo "Valor $i: ". $$v ."<br/>";
        $i++;
    }        
    ?>
    <br>
    <p>Os comandos abaixo existem mas são poucos usados e poucos recomendados</p>
    <img src="imagens/modif_laco.png" alt="">
</body>
</html>