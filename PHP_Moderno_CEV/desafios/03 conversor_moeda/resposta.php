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
            $numero = $_GET["numero"] ?? "Voce não informou o numero"; //variável superglobal que contem todos os dados que vem da emissão do formulário 
            $cotacao = 5.22;
            $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY); //FORMA INTERNACIONALIZADA DE FORMATAR   
            $vr_convertido = $numero / $cotacao; 
            //$numero = number_format($numero, 2,',','.');//FORMA SIMPLES DE FORMATAR 
            $numero = numfmt_format_currency($padrão, $numero, "BRL");
            // $dolar = number_format($vr_convertido, 2, ',','.' );
            $dolar = numfmt_format_currency($padrão, $vr_convertido, "USD");
            echo "<h1>Conversor de moedas v1.0</h1>";      
            echo "<p>Seus <strong>$numero </strong> equivalem a <strong>$dolar</strong>";
            echo "<p>Cotação fixa de <strong>R$5,22</strong> informada diretamente no código</p>"            
        ?>
        <button onclick="javascript:history.go(-1)">Voltar</button> 
    </main>
</body>
</html>