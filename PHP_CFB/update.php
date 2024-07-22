<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php
    include "conexao.inc";
    $sql="update tb_cadastro set telefone='(33)93333-6445' where cod = '16'";
    $atualiza=mysqli_query($con, $sql);

    $linhas=mysqli_affected_rows($con);

    if($linhas == 1) {
        print "Registro atualizado com sucesso ";
    } else {
        print "Registro não encontrado ou atualização ja feita";
    }

    mysqli_close($con);
?>
    
</body>
</html>