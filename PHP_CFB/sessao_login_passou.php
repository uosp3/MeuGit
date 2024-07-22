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
        session_start();

        if (isset($_SESSION["numLogin"])) {
            $n1=$_GET["num1"];
            $n2=$_SESSION["numLogin"];
            if($n1 != $n2) {
                print "Login não efetuado!";
                exit;
            } 
        } else {
            print "Login não efetuado!";
            exit;
        }

       session_destroy(); 
    include "conexao.inc";
        print $_SESSION['username']." Voce está logado!";
 
    mysqli_close($con);
 ?>

</body>
</html>