<?php
$con=mysqli_connect("localhost", "root", ""); // host, usaername, senha
mysqli_select_db($con,"canalfb");// conexão, banco de dados

$vnome="Bruno";
$vuser="brra8";
$vsenha="94949";
$vmail="qqum@naosei.com";
$vtel="0800";
$vst=1;
$vobs="tudo certo";

$sql="INSERT INTO tb_cadastro VALUES (NULL, '$vnome', '$vuser', '$vsenha', '$vmail', '$vtel', $vst, '$vobs')"; // para números ($vst) não usa apóstrofo (aspas)
$rs=mysqli_affected_rows($con); // quantidade de registros inseridos

$insere=mysqli_query($con, $sql);

$consulta=mysqli_query($con, "SELECT * FROM tb_cadastro");// consulta
$linhas=mysqli_num_rows($consulta); //pega numero de linhas da consulta

print "$rs registro(s) inserido(s), tem $linhas registro(s) na tabela tb_cadastro";

mysqli_close($con);// depois de usar fecha a conexão.

?>



<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 28 de PHP - Conexão com Banco de Dados.</title>
</head>
<body>
    
</body>
</html>