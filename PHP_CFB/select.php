<?php
    include "conexao.inc";
    $vcat1=$_POST['s_cat1'];
    $vcat2=$_POST['s_cat2'];

    $sql="SELECT * FROM tb_produtos WHERE cat = $vcat2 OR cat = $vcat1";    
    $consulta = mysqli_query($con, $sql);
    $linhas = mysqli_num_rows($consulta);
    print "$linhas registro(s) encontrado(s)";    
?>



<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table, tr, td, th {
            border: 1px solid black;            
        }

        th {
            text-align: center;            
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>Codigo</th>
            <th>Produto</th>
            <th>Preço</th>
            <th>Quant</th>
            <th>Categ</th>
        </tr>
    
    <?php
        while($registro=mysqli_fetch_row($consulta)) { //pega registro por registro da consulta
            $vcod=$registro[0];
            $vprod=$registro[1];
            $vpreco=$registro[2];
            $vqtde=$registro[3];
            $vcat=$registro[4];
            print "<tr>";
            print "<td>$vcod</td>";
            print "<td>$vprod</td>";
            print "<td> $vpreco</td>";
            print "<td> $vqtde</td>";
            print "<td> $vcat</td>";
            print "</tr>";
        }    
    
    ?></table>
<p><a href="select_form.html"> voltar</a></p>
</body>
</html>
<?php
mysqli_close($con);
?>