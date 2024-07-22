<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 18 de PHP - Passagem de valores pela URL</title>
</head>
<body>
<?php
$texto = "Curso de PHP";
$nome = "Edson";
$canal = "vlog do professor Bruno";

print "<a href=passa_vr_url2.php?tx=".urlencode($texto)."&no=".urlencode($nome)."&cn=".urlencode($canal).">Abre Pagina 1</a>";

?>
    
</body>
</html>
