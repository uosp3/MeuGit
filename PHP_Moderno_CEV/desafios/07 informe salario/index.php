<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercicio PHP</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        //Capturando os dados do formulário retroalimentado
        $salmin = 1_380.60;
        $salario = $_GET['salario'] ?? $salmin; 
        $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY);       
    ?>
    <main>
        <h1>Informe seu salário</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF']?>-->
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="v1">Salário</label>
            <input type="number" name="salario" id="salario" value="<?=$salario?>" step=".01">
            <p>Considerando o salário mínimo de <strong><?= numfmt_format_currency($padrão, $salmin, "BRL")?></strong></p>
            <input type="submit" value="Calcular">
        </form>
    </main>   
        <?php            
                echo "<section id='resultado'>";
                echo "<h2>Resultado Final</h2>";
                $qtsalarios = (int)($salario/$salmin);
                $sobra = $salario%$salmin;
                print "<p>Quem recebe um salário de " . numfmt_format_currency($padrão, $salario, "BRL") . " ganha $qtsalarios salário(s) mínimo(s) + " . numfmt_format_currency($padrão, $sobra, "BRL") . "</p>";
                echo "</section>";            
        ?>    
</body>
</html>
