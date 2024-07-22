<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php      
    
        $vmail = $_POST['email_txt'];
        $vassunto = $_POST['assunto_txt'];
        $vmsg = $_POST['msg_txt'];

        print "$vmail  =====  $vassunto ===== $vmsg";

        if (mail($vmail, $vassunto,$vmsg)) {
            print "Mensagem enviada";
        } else {
            print "Erro ao enviar, tente novamente";   
        }

    ?>
</body>
</html>