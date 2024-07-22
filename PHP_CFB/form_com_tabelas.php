<?php
    include "conexao.inc";



?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Pesquisa</h1>
    <form action="form_com_tab_processa.php" name="fcad" method="GET">
        <label for="">Nome</label><br>
        <input type="text" name="fnome" required><br><br>
        <label for="">Selecione seu estado:</label><br>
        <select name="fuf" id="">
            <?php
                $sql="select * from tb_uf order by uf";
                $consulta=mysqli_query($con, $sql);
                while($vreg=mysqli_fetch_row($consulta)) {
                    $vuf=$vreg[0];
                    $vsigla=$vreg[1];
                    print "<option value=$vsigla>$vuf</option>";
                }
            ?>
        </select>
        <br><br>

        <label for="">Selecione seus meios de transporte favoritos</label><br>
        <?php
                $sql="select * from tb_transportes";
                $consulta=mysqli_query($con, $sql);
                while($vreg=mysqli_fetch_row($consulta)) {
                    $vcod=$vreg[0];
                    $vtransporte=$vreg[1];
                    print "<input type=checkbox name=ftransp[] value=$vcod id=$vtransporte><label for=$vtransporte>$vtransporte</label><br>";
                    //id do checkbox = for do label para que ao clicar no nome o checkbox seja selecionado.
                }
            ?>
        <br>

        <input type="submit" value="Gravar Pesquisa">
        
    </form>
</body>
</html>
<?php
    mysqli_close($con);
?>