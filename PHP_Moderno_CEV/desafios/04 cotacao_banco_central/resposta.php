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
            //////////////////////////////////////////////////////
            //cotação vinda do Banco Central do Brasil
                $inicio = date("m-d-Y", strtotime("-7 days"));
                $fim = date("m-d-Y");
                $url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=\''. $inicio .'\'&@dataFinalCotacao=\''. $fim .'\'&$top=1&$orderby=dataHoraCotacao%20desc&$format=json&$select=cotacaoCompra,dataHoraCotacao';
            
                $dados = json_decode(file_get_contents($url), true);
            
                $cotação = $dados["value"][0]["cotacaoCompra"];
            //////////////////////////////////////////////////////
         
            $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY); //FORMA INTERNACIONALIZADA DE FORMATAR   
            $vr_convertido = $numero / $cotação; 
            //$numero = number_format($numero, 2,',','.');//FORMA SIMPLES DE FORMATAR 
            $numero = numfmt_format_currency($padrão, $numero, "BRL");
            $cotação = numfmt_format_currency($padrão, $cotação, "BRL");

            // $dolar = number_format($vr_convertido, 2, ',','.' );
            $dolar = numfmt_format_currency($padrão, $vr_convertido, "USD");
            echo "<h1>Conversor de moedas v2.0</h1>";      
            echo "<p>Seus <strong>$numero </strong> equivalem a <strong>$dolar</strong>";
            echo "<p>Cotação do dolar hoje <strong>$cotação</strong> - Fonte BC do Brasil</p>"            
        ?>
        <button onclick="javascript:history.go(-1)">Voltar</button> 
    </main>
</body>
</html>