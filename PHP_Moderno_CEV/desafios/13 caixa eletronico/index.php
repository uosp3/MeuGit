<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercicio PHP</title>
    <link rel="stylesheet" href="style.css">
    <style>
        img.nota {
            height: 50px;
            margin: 5px;
        }
    </style>
</head>

<body>
    <?php
    //Capturando os dados do formulário retroalimentado
    $total = $_GET['total'] ?? 0;
    
    $cem = (int)($total / 100);
    //$cem = floor($total/100) ==== Faz o mesmo que a linha acima, arredonda para baixo
    $resto = $total % 100;

    $cinquenta = (int)($resto / 50);
    $resto %= 50;

    $vinte = (int)($resto / 20);
    $resto %= 20;

    $dez = (int)($resto / 10);
    $resto %= 10;

    $cinco = (int)($resto / 5);
    ?>
    <main>
        <h1>Caixa Eletrônico</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF'] ?>-->
        <form action="<?= $_SERVER['PHP_SELF'] ?>" method="get">
            <label for="">Qual valor você deseja sacar? (R$)<sup>*</sup></label>
            <input type="number" name="total" id="total" step="5" value="<?= $total ?>" required>
            <p style="font-size: 0.7em">* Notas disponíveis: R$100, R$50, R$20, R$ 10 e R$5</p>
            <input type="submit" value="Sacar">
        </form>
    </main>
    <section id='resultado'>
        <h2>Saque de <?= number_format($total, 2, ',', '.') ?> realizado </h2>
        <p>O Caixa eletrônico vai de entregar as seguinte notas:</p>
        <ul>
            <li><img src='cem.jpg' class='nota'> X <?= $cem ?></li>
            <li><img src='cinquenta.jpg' class='nota'> X <?= $cinquenta ?></li>
            <li><img src='vinte.jpg' class='nota'> X <?= $vinte ?></li>
            <li><img src='dez.jpg' class='nota'> X <?= $dez ?></li>
            <li><img src='cinco.jpg' class='nota'> X <?= $cinco ?></li>
        </ul>
    </section>
</body>

</html>