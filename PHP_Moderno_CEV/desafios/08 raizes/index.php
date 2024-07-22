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
        $numero = $_GET['numero'] ?? 0; 
       
        $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY);       
    ?>
    <main>
        <h1>Informe um número</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF']?>-->
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="v1">Número</label>
            <input type="number" name="numero" id="numero" value="<?=$numero?>">            
            <input type="submit" value="Calcular Raizes">
        </form>
    </main>   
    <section id='resultado'>
        <h2>Resultado Final</h2>        
        <?php
        $raizquadrada = number_format(sqrt($numero),2,',','');
        $raizcubica = number_format($numero ** (1/3), 2,',','');            
            print "<p>Analisando o <strong>número $numero</strong>, temos:</p>";
            print "<ul><li>A sua raiz quadrada é $raizquadrada </li>";
            print "<li>A sua raiz cúbica é $raizcubica</li></ul>";
        ?>    
    </section>            
</body>
</html>
