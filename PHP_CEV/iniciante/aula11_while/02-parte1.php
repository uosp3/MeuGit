<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Criando conteúdos dinâmicamente </h1>
    <form action="02-parte2.php" method="GET">
     <?php 
        $c = 1;  
        while ($c <=5) {       
            echo "Valor $c: <input type='number' name='v$c' max='100' min='0' value='0'><br>";
        $c++;}
        ?>
        <input type="submit" value="Enviar">
    </form>    
    <br>
    <img src="" alt="">
</body>
</html>