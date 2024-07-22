<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modelo</title>
    <link rel="stylesheet" href="../estilos/style.css">
</head>
<body>
    <h1>Assunto: Vota ou não vota</h1>
    <?php
        $a = isset($_GET["ano"]) ? $_GET["ano"] : 1900;
        $i = date("Y") - $a;
        echo "Você nasceu em $a e tem $i anos. <br>";
        if ($i<16){
            $tipoVoto = "não vota";
        } else { // o if abaixo pode subir e ficar nesta linha como elseif e desta forma eliminar um bloco de chaves.
            if (($i >=16 && $i<18) || ($i > 65)){
                $tipoVoto = "voto opcional";
            } else {
                $tipoVoto = "voto obrigatório";
            }
        }
        echo "Com essa idade $tipoVoto ";
    ?>
    <br>
    <img src="" alt="">
</body>
</html>