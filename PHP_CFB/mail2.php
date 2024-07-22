<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 26 de PHP - Enviando e-mail</title>
</head>
<body>
    <form action="mail.php" method="post" name="email">
        <label for="">e-mail</label><br>
        <input type="text" name="email_txt" id=""><br>
        <label for="">Assunto</label><br>
        <input type="text" name="assunto_txt" id=""><br>
        <label for="">Mensagem</label><br>
        <textarea name="msg_txt" id="" cols="30" rows="10"></textarea><br><br>
        <input type="submit" value="Enviar">

    </form>
</body>
</html>