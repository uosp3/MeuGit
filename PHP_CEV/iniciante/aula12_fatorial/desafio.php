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
    <h1>Taboada</h1>
    <form action="taboada.php" method="GET">        

     <?php 
     //Criando conteúdos dinâmicamente. 
        echo "Número: <select name='numero' id=''>";               
        $c = 1;  
        while ($c <=10) {       
            echo "<option value='$c'>$c</option>";
        $c++;}
        // fim do conteúdo dinâmico
        "</select>";
        ?>
        <input type="submit" value="Taboada">
    </form>    
    <br>
    <img src="" alt="">
</body>
</html>