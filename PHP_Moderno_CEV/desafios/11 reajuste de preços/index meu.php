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
    $oculto = $_GET['oculto'] ?? 0;  
    $padrão = numfmt_create("pt_BR", NumberFormatter::CURRENCY);
    

    ?>
    <main>
        <h1>Reajustador de Preços</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF'] ?>-->
        <form action="<?= $_SERVER['PHP_SELF'] ?>" method="get">
            <label for="preco">Preço do Produto (R$)</label>
            <input type="number" name="precoinicial" id="precoinicial" required step="0.01" value="<?=$precoinicial?>" required>
            <input type="hidden" value="<?=$oculto?>" name="oculto" id="oculto" class="oculto">

            <label for="preco">Qual será o percentual de reajuste? (<strong><span><?=$oculto?></span>%</strong>)</label>
            <input type='range' value='<?=$oculto?>' max='100' id="deslisa" class="deslisa">
            
            <input type="submit" value="Reajustar">
        </form>
    </main>
    <section id='resultado'>
        <h2>Resultado do Reajuste</h2>
        <?php
        $precofinal = $precoinicial*($oculto/100)+$precoinicial;
        print "<p>O produto que custava " . numfmt_format_currency($padrão, $precoinicial, "BRL") . " com <strong>$oculto% de aumento</strong> vai passar a custar <strong>" . numfmt_format_currency($padrão, $precofinal, "BRL") . "</strong> a partir de agora  </p>";
        ?>
    </section>
</body>

</html>

<script>
    var $range = document.querySelector('#deslisa'),
        $oculto = document.querySelector('#oculto'),
        $value = document.querySelector('span');
    
    $range.addEventListener('input', function() {
      $value.textContent = this.value;
      $oculto.value = this.value;
    });
</script>