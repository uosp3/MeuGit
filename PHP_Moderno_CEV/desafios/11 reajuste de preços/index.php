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
    $precoinicial = $_GET['precoinicial'] ?? 0; 
    $reaj = $_GET['reaj'] ?? 0;  
        
    ?>
    <main>
        <h1>Reajustador de Preços</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF'] ?>-->
        <form action="<?= $_SERVER['PHP_SELF'] ?>" method="get">
            <label for="preco">Preço do Produto (R$)</label>
            <input type="number" name="precoinicial" id="precoinicial" required step="0.01" value="<?=$precoinicial?>" required>
            
            <label for="reaj">Qual será o percentual de reajuste? (<strong><span id="p">?</span></strong>%)</label>
            <input type='range' name="reaj" id="reaj" max='100' step="1" oninput="mudaValor()" value="<?=$reaj?>">
            
            <input type="submit" value="Reajustar">
        </form>
    </main>
    <?php 
        $aumento = $precoinicial * $reaj/100;
        $precofinal = $precoinicial + $aumento
    ?>
    <section id='resultado'>
        <h2>Resultado do Reajuste</h2>
        <p>O produto que custava R$<?=number_format($precoinicial,2,',','.')?>, com <strong><?=$reaj?>% de aumento</strong> vai passar a custar <strong>R$<?=number_format($precofinal,2,',','.')?></strong></p>
    </section>    
    <script>
        mudaValor()
        function mudaValor(){
            p.innerText = reaj.value;
        }
    </script>
</body>
</html>