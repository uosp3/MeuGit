<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário para login</title>
</head>
<body>
 <?php
        // o ideal é usar o trecho abaixo em um arquivo include
        if (isset($_COOKIE["numLogin"])) {
            $n1=$_GET["num1"];
            $n2=$_COOKIE["numLogin"];
            if($n1 != $n2) {
                print "Login não efetuado!";
                exit;
            } 
        } else {
            print "Login não efetuado!";
            exit;
        }

        
    include "conexao.inc";
        print "Voce está logado!";
 
    mysqli_close($con);
 ?>

</body>
</html>