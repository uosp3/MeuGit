<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trabalhando com arquivos</title>
</head>
<body>
    <?php
    // r = abre p/ leitura, ponteiro no início
    // r+ = abre p/ leitura e escrita
    // w = abre p/ escrita, ponteiro no início e zera, se não existir cria
    // w+ = abre p/ leitura e escrita
    // a = abre p/ escrita, ponteiro no final, se não existir cria
    // a+ = abre p/ leitura e escrita
    // x = abre p/ escrita, ponteiro no início, se existir gera erro tipo E_WARNING
    // x+ = abre p/ leitura e escrita

    $arquivo = fopen("aula.txt","r+");// abre e/ou cria o arquivo
    fwrite($arquivo, "\r\n Eu to maluco");// escrevendo no arquivo

    $arquivo = fopen("aula.txt", "r");
    $conteudo = fread($arquivo, 1000); //lê o conteúdo do arquivo (100 é qtde de bites)
    
    print $conteudo;

    fclose($arquivo);
    
    
    ?>
    
</body>
</html>