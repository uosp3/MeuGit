<?php
    include "conexao.inc";

    $sql="Delete FROM tb_cadastro WHERE cod = '7'";
    $delete=mysqli_query($con, $sql);

    $linhas=mysqli_affected_rows($con); //linhas afetadas pelo comando
    print "$linhas registro(s) excluido(s)";

    mysqli_close($con);
?>