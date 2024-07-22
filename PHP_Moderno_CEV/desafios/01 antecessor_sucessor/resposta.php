<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Resultado Final.</h1>
        <?php 
            //var_dump($_GET);
            //var_dump($_POST)
            //var_dump($_REQUEST) // $_GET $_POST $_COOKIES
            $numero = (int)$_REQUEST["numero"] ?? 0; //variável superglobal que contem todos os dados que vem da emissão do formulário
            echo "<p>O númemro escolhido foi <strong>$numero </strong></p>";
            echo "<br>O seu <em>antecessor</em> é <strong>" . $numero - 1 ."</strong>";
            echo "<br>O seu <em>sucessor</em> é <strong>" . $numero + 1 ."</strong>";  
        ?>
        <button onclick="javascript:history.go(-1)">&#x2b05; Voltar</button> 
        <button onclick="javascript:window.location.href='index.html'">&#x2b05; Voltar 2</button> 
    </main>
</body>
</html>