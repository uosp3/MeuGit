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
        $dividendo = $_GET['dividendo'] ?? 0;
        $divisor = $_GET['divisor'] ?? 1;
    ?>
    <main>
        <h1>Anatomia de uma Divisão</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF']?>-->
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="v1">Dividendo</label>
            <input type="number" name="dividendo" id="dividendo" value="<?=$dividendo?>" min="0">
            <label for="v2">Divisor</label>
            <input type="number" name="divisor" id="divisor" value="<?=$divisor?>" min="1">
            <input type="submit" value="Analisar">
        </form>
    </main>   
        <section>
            <h2>Estrutura da Divisão</h2>
            <?php 
                $quociente= intdiv($dividendo, $divisor);
                $resto = $dividendo % $divisor
            ?>
            <table class="divisao">
                <tr>
                    <td><?=$dividendo?></td>
                    <td><?=$divisor?></td>
                </tr>
                <tr>
                    <td><?=$resto?></td>
                    <td><?=$quociente?></td>
                </tr>
                
            </section>
        </table>   
</body>
</html>