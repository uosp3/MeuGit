<?php
include "conexao.inc";

$vnome=$_GET['fnome'];
$vuf=$_GET['fuf'];
$vtrans_temp=array(0,0,0,0);

print "Nome: $vnome - Estado: $vuf<br>";
print "Transportes selecionados:<br>";

foreach($_GET['ftransp'] as $transporte) { //joga os checkbox passados(so os marcados) em $transporte
    $vtrans_temp[$transporte-1]=1;// os checkbox tem valores de 1 a 4, por isto o menos um (-1) para o array ficar certo, ou seja, começando em zero.
    print "$transporte<br>";
}
print "<hr>";

$sql="insert into tb_pesquisa values (null, '$vnome', '$vuf', '$vtrans_temp[0]', '$vtrans_temp[1]', '$vtrans_temp[2]', '$vtrans_temp[3]')";
$insere=mysqli_query($con, $sql);

print "Pesquisa gravada <br>";
print "<a href='form_com_tabelas.php'>Voltar</a>";

mysqli_close($con);
?>