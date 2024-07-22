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
        $nasceu = $_GET['nasceu'] ?? 1900; 
        $anonovo = $_GET['anonovo'] ?? date('Y');
    ?>
    <main>
        <h1>Calculando a sua idade</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF']?>-->
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nasceu">Em que ano voce nasceu?</label>
            <input type="number" name="nasceu" id="nasceu" value="<?=$nasceu?>" min="1900" max="<?= date('Y')-1?>" required>
            <label for="anonovo">Quer saber sua idade em que ano? (atualmente estamos em <?= date('Y')?>)</label>
            <input type="number" name="anonovo" id="anonovo" value="<?=$anonovo?>" min="<?= date('Y')?>" required>
            
            <input type="submit" value="Qual será minha idade?">
        </form>
    </main>   
    <section id='resultado'>
        <h2>Resultado</h2>        
        <?php
        $novaidade = $anonovo-$nasceu;                  
            print "<p>Quem nasceu em $nasceu vai ter <strong>$novaidade anos</strong> em $anonovo</p>";            
        ?>    
    </section>            
</body>
</html>
