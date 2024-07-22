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
    <header>
        <h1>Resultado do processamento</h1>
    </header>
    <main>
        <?php 
            //var_dump($_GET);
            //var_dump($_POST)
            //var_dump($_REQUEST) // $_GET $_POST $_COOKIES
            $nome = $_GET["nome"] ?? "Se não for passado o nome"; //variável superglobal que contem todos os dados que vem da emissão do formulário
            $sobrenome = $_GET["sobrenome"] ?? "Nada foi informado";
            echo "<p>É um prazer te conhecer <strong>$nome $sobrenome</strong>! Este é o meu site!"
        ?>
        <p><a href="javascript:history.go(-1)">Voltar</a></p>
    </main>
</body>
</html>