<?php
$vcod = $_POST["f_cod"];
$vprod = $_POST["f_prod"];
$vpreco = $_POST["f_preco"];
$vqtde = $_POST["f_qtde"];
$vcat = $_POST["f_cat"];

$value1 = $_POST["f_cod"];
$value2 = $_POST["f_prod"];
$value3 = $_POST["f_preco"];
$value4 = $_POST["f_qtde"];
$value5 = $_POST["f_cat"];

$con=mysqli_connect("localhost", "root", ""); // host, usaername, senha
mysqli_select_db($con,"canalfb");// conexão, banco de dados

$sql="INSERT INTO tb_produtos VALUES ('$vcod', '$vprod', '$vpreco', '$vqtde', '$vcat')"; // serve este e tb a linha abaixo.....

//$sql="INSERT INTO `tb_produtos`(`codigo`, `produto`, `preco`, `qtde`, `cat`) VALUES ('$value1','$value2','$value3','$value4', '$value5')";

$insere=mysqli_query($con, $sql);
$linhas = mysqli_affected_rows($con);

if ($linhas== 1) {
    print "Registro gravado com sucesso";
} else {
    print "Falha na gravação do registro";
}

mysqli_close($con);

?>