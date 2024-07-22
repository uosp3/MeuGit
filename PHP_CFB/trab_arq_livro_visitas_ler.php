<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Livro de visitas</title>
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
     
        $arquivo = fopen("visitas.txt", "r"); //abre o arquivo
        while(!feof($arquivo)) {//f end of file, lê até que chega no final do arquivo
            print fgets($arquivo, 4096); //lê a linha, bites
            print "<br>".fgets($arquivo, 100); //lê a próxima linha, bites
            print "<hr>";        
        }
        fclose($arquivo);
    ?>
    <hr>
    <a href="trab_arq_livro_visitas.html">Voltar</a>

</body>
</html>