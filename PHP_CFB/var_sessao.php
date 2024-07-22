<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Variáveis de sessão.</title>
</head>
<body>
    <a href="var_sessao2.php">Próxima Página</a>
</body>
</html>
<?php
    session_start(); // inicião a sessão, para variáveis de sessão
    //session_destroy(); ====> destroi a sessão iniciada.

    $_SESSION['vnome'] = "Edson"; // criou uma variário de sessão.



?>