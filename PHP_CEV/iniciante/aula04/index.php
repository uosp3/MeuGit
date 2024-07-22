<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 04 - Variáveis e concatenação</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Curso de PHP para iniciantes</h1>    
    <div>
        <?php
        //variáveis
           $idade = 61;
           $nome = "Edson";
           echo $nome. " tem ". $idade. " anos!"; // concatenação
           echo "<br>$nome tem $idade anos!!!"; //pode ser feito assim tb, sem a concatenação
        ?>
        <img style="display: block;" src="imagens/typecast.png" alt="typecast">
    </div>
</body>
</html>