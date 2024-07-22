<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contar acessos</title>
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
    
    $arquivo=fopen("contador.txt", "a+"); //abre para leitura
    $cont = fread($arquivo, 21); //lê o arquivo
    $cont++; //soma 1
    $arquivo=fopen("contador.txt", "w"); //abre para escrita e zera
    fwrite($arquivo, $cont);// escreve o novo valor no arquivo.
    fclose($arquivo);

    print "Quantidade de acessos: $cont <br>";
    ?>
    
</body>
</html>