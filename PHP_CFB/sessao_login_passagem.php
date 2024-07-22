<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário para login - com var sessão</title>
</head>
<body>
 <?php
    include "conexao.inc";

    $user=$_POST['f_user'];
    $senha=$_POST['f_senha'];

    $sql="select * from tb_cadastro where username='$user' and senha='$senha'";
    $consulta=mysqli_query($con, $sql);
    $linha=mysqli_affected_rows($con);

    if($linha > 0) {
        $num=rand(100000, 900000);

        session_start();
        $_SESSION['numLogin']=$num;
        $_SESSION['username']=$user;
       
        header("Location:sessao_login_passou.php?num1=$num");        
    } else {
        print "ERRO usuário ou senha inválido!";
        print "<br><a href='sessao_login.html'>Voltar</a>";
    }
    mysqli_close($con);
 ?>

</body>
</html>