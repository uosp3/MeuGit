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
    $total = $_GET['total'] ?? 0;

    $semanas = $total / 604800;
    $resto = $total % 604800;

    $dias = $resto / 86400;
    $resto = $resto % 86400;

    $horas = $resto / 3600;
    $resto = $resto % 3600;

    $minutos = $resto / 60;
    $resto = $resto % 60;

    $segundos = $resto;

    $semanas = (int)$semanas;
    $dias = (int)$dias;
    $horas = (int)$horas;
    $minutos = (int)$minutos;

    //semanas = 7*24*60*60 = 604800
    //dias = 24*60*60 = 86400
    //horas = 60*60 = 3600
    //minutos = 60

    ?>
    <main>
        <h1>Calculadora de tempo</h1>
        <!-- a linha abaixo é uma forma simplificada quando há apenas um comando dentro da supertag php, ela equivale a: <?php echo $_SERVER['PHP_SELF'] ?>-->
        <form action="<?= $_SERVER['PHP_SELF'] ?>" method="get">
            <label for="preco">Qual é o total de segundos?</label>
            <input type="number" name="total" id="total" required value="<?= $total ?>" required>
            <input type="submit" value="Calcular">
        </form>
    </main>
    <section id='resultado'>
        <h2>Totalizando tudo</h2>
        <p>Analisando o valor que voce digitou, <?= number_format($total, 0, ",", ".") ?>  segundos equivalem a um total de:</p>
        <ul>
            <li><?=$semanas?> semanas</li>
            <li><?=$dias?> dias</li>
            <li><?=$horas?> horas</li>
            <li><?=$minutos?> minutos</li>
            <li><?=$segundos?> segundos</li>
        </ul>
    </section>
</body>

</html>