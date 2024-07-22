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
        <?php 
            //var_dump($_GET);
            //var_dump($_POST)
            //var_dump($_REQUEST) // $_GET $_POST $_COOKIES
            $numero = $_GET["numero"] ?? 0; 
            //$numero = isset($_GET["numero"]) ? $_GET["numero"] : 0; 

            //variável superglobal que contem todos os dados que vem da emissão do formulário 
            $inteiro = number_format((int)$numero,0, ',','.');    
            $fracao = number_format(($numero - (int)$numero),3,',',''); 
            $numero = number_format($numero,3,',','.'); 
            //number_format($fracao, 3, '.','' );
            echo "<h1>Analisador de Número Real</h1>";      
            echo "<p>Analisando o número <strong>$numero </strong> informado pelo usuário:";
            echo "<ul><li>A parte inteira do número é  <strong>$inteiro</strong></li>";
            echo "<li>A parte fracionária do número é  <strong>$fracao </strong></li></ul>";  
        ?>
        <button onclick="javascript:history.go(-1)">Voltar</button> 
    </main>
</body>
</html>