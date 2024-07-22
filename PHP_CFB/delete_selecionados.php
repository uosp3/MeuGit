<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deletando selecionados</title>
    <style>
        table, tr, td, th {
            border: 1px solid black;
        }
        th {
            background-color: gray;
            color: white
        }
        .centro {
            text-align: center;
        }
    </style>
</head>
<body>
    <form action="delete_selecionados.php" method="POST">
        <table>
            <tr>
                <th>Codigo</th>
                <th>Nome</th>
                <th>Selecionar</th>
            </tr>
            <?php
                include "conexao.inc";

                if (isset($_POST['sel'])) {// verifica se o sel ja existe
                    Print "Formulário foi submentido";
                    foreach($_POST['sel'] as $vcodigo) {
                        $sql="delete from tb_cadastro where cod=$vcodigo";
                        $delete=mysqli_query($con, $sql);
                    }
                } else {
                    print "Formulário não submetido";
                }                

                $sql="select * from tb_cadastro order by cod";
                $consulta=mysqli_query($con, $sql);

                while($vregistro=mysqli_fetch_row($consulta)){
                    $vcod=$vregistro[0];
                    $vnome=$vregistro[1];

                    print "<tr>";
                    print "<td>$vcod</td>";
                    print "<td>$vnome</td>";
                    print "<td class='centro'><input type='checkbox' name='sel[]' id='' value='$vcod'></td>"; // esse sel[] é verificado lá no foreach
                    print "</tr>";
                }    
              mysqli_close($con)             
            ?>    
             
        </table>
        <br>       
        <input type="submit" value="Excluir" name="bt_excluir">
    </form>
</body>
</html>