<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Variáveis de sessão.</title>
</head>
<body>
    <?php
        session_start();//para manter a variável de sessão que foi criada na pag anterior.
        if($_SESSION['vnome'] == "Edson") {
            print "Variável de sessão ". $_SESSION['vnome'] ." recebida com sucesso ";
            session_destroy();
        } else {
            print "Nenhuma variável de sessão econtrada";
        }

    ?>
</body>
</html>