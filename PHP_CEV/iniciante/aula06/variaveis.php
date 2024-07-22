<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aprendendo PHP</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Variáveis referenciadas</h1><br>
    <img src="imagens/var_referenciadas.png" alt="incremento">
    
    <br><br>
    <h1>Variáveis de variáveis</h1><br>
    <img src="imagens/var_variaveis.png" alt="incremento">

    <?php
        $x = "edson";
        $$x = "Santos"; //nesse caso é criada uma variável com o nome $edson, que é o valor atribuido a $x.
        echo "<br>O conteúdo da variável X é $x";
        echo "<br>A variável criada ($".$x.")recebeu o valor $edson";
    ?>

</body>
</html>