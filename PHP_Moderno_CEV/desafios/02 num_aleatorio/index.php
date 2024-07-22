<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Numeros aleatórios</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>    
    <section>
        <!-- <form action="index.php" method="get"> -->
            <h1>Trabalho com números aleatórios mt_rand()</h1>   
            <p>Gerando número aleatório entre 0 a 100...</p>
            <?php 
                $numero = mt_rand(1,100);
                echo "<p>O valor gerado foi <strong>$numero</strong></p>"                
            ?>
            <button onclick="javascript:document.location.reload()">&#x1f504; Gerar outro</button>            
            <!-- <input type="submit" value="Gerar Número"> -->
        <!-- </form> -->
    </section>
</body>
</html>