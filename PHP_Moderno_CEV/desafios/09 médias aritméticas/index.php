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
        $v1 = $_GET['v1'] ?? 0; 
        $v2 = $_GET['v2'] ?? 0; 
        $p1 = $_GET['p1'] ?? 1; 
        $p2 = $_GET['p2'] ?? 1; 
       
        $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY);       
    ?>
    <main>
        <h1>Médias Aritméticas</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF']?>-->
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="v1">1º valor</label>
            <input type="number" name="v1" id="v1" value="<?=$v1?>" min="1" required>
            <label for="v1">1º peso</label>
            <input type="number" name="p1" id="p1" value="<?=$p1?>" min="1" required>

            <label for="v1">2º valor</label>
            <input type="number" name="v2" id="v2" value="<?=$v2?>" min="1" required>"
            <label for="v1">2º peso</label>
            <input type="number" name="p2" id="p2" value="<?=$p2?>" min="1" required>
            

            <input type="submit" value="Calcular Médias">
        </form>
    </main>   
    <section id='resultado'>
        <h2>Cálculo das Médias</h2>        
        <?php
        $mediasimples = number_format(($v1+$v2)/2,2,',','');
        $mediaponderada = number_format(($v1*$p1 + $v2*$p2)/($p1+$p2),2,',','');            
            print "<p>Analisando os valores $v1 e $v2:</p>";
            print "<ul><li>A <strong>Média Aritmética Simples</strong> entre os valores é igual a $mediasimples.</li>";
            print "<li>A <strong>Média Aritmética Ponderada</strong> com os pesos $p1 e $p2 é igual a $mediaponderada.</li></ul>";
        ?>    
    </section>            
</body>
</html>
