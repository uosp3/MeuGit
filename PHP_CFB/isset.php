<?php
    // o formulário desaparece depois que os dados são submetidos.
    if (isset($_POST["f_nome"])) {
        $vnome = $_POST["f_nome"];
        print "Nome:  $vnome <br>";
    } else {
        print "Dados não submetidos";
    
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 17 de PHP - Isset</title>
</head>
<body>
    <form action="isset.php" method="post"> <!--a pagina chamando ela mesma.-->
        <label for="">Nome:</label>
        <input type="text" name="f_nome" id="" required><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>

<?php
    }//fechamento do if la de cima
?>