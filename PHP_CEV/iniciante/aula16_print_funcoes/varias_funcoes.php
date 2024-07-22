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
    <h1>wordwrap</h1>
    
    <?php
        $t = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Molestiae voluptatibus nihil cumque in veritatis et rem enim non optio. Nesciunt iste explicabo at maiores similique aspernatur cumque in unde earum!";
        $acentos = "ÁÉÍÓÚáéíóúÀÈÌÒÙàèìòùÂÊÎÔÛâêîôûÇÑÃÕçñãõÄËÏÖÜäëïöüªº";
        // WORDWRAP
        $r = wordwrap($t, 60, "<br>\n", false);        
        // no caso acima o '60' indica em quantas letras o texto será quebrado. O <br> faz a quebra visual na página mas não no código fonte. O \n faz a quebra na página e no código fonte. O TRUE faz a quebra da palavra independente do tamanha dela, mas o FALSE não quebra as palavras.
        print "<hr>$r<br>";
        
        print "<hr><br>";

        //STRLEN OU MB_STRLEN
        $txt = "Curso em vídeo";
        print mb_strlen ($txt); //o normal seria apenas STRLEN mas isso conta as letras acentuadas como se fossem duas letras.
        print "<hr><br><br>";
        $tr = "        Edson Gomes dos Santos "; //digitado com espaços antes e depois
        print strlen($tr); // mostra a quantidade caracteres, considerando os espaços.
        print "<hr><br>";
       
        //TRIM, LTRIM, RTRIM
        print trim($tr);// Faz o corte dos espaços da esquerda e da direita, para o caso de cortar espaços apenas de um dos lados pode usar LTRIM ou RTRIM
        print "<hr><br>";

        //STR_WORD_COUNT
        print str_word_count("Edson Gomes dos Santos", 0); // conta as palavras da string. Se o zero for trocado por 1 retorna um vetor (array). Se trocar por 2, tb gera um array mas com a posição inicial de cada palavra dentro da frase.
        print"<br>";
        print_r (str_word_count("édson Gomês dos Santõs", 1, $acentos));//a variável "$acentos" foi criada para evitar erros, pois o comando não os reconhece se não forem indicados.
        print"<br>";
        print_r (str_word_count("édson Gomês dos Santôs", 2, $acentos));
        print "<hr><br>";  
        
        //EXPLODE
        $nome = "Edson Gomes dos Santos";
        $vetor = explode(" ", $nome); //os espaços " " é o caractere que irá dividir a string em array, pose ser usado qualquer caractere no lugar do espaço.
        print_r($vetor);
        print "<hr><br>";  

        //STR_SPLIT
        $eu = "Edson";
        $vetor2 = str_split($eu);// transforma cada letra em um componente de um array, cada letra com um indece separado do array
        print_r($vetor2);
        print "<hr><br>"; 

        //IMPLODE ou JOIN
        $vetor[0] = "Edson";
        $vetor[1] = "Gomes";
        $vetor[3] = "Santos";
        $texto = implode("-", $vetor);//Junta todos os vetores em um so, o hífem "-" pode ser subtituido por qualquer caractere.
        print($texto);
        print "<hr><br>"; 

        //CHR
        $letra = chr(67);// retorna a letra correspondente ao código, no caso 67.
        print "A letra de código 67 é $letra";
        print "<hr><br>"; 

        //ORD
        $num = "E";
        $cod = ord($num);// retorna o código da letra, no caso "E" que é 69.
        print "A letra $num tem código $cod";
        print "<hr><br>"; 

        //STRTOLOWER
        $nome = "EdSon GoMEs dos SANTOS";
        print "Seu nome em minúsculo é ".strtolower($nome);//passa tudo para MINÚSCULO, existe um problema com caracteres acentuados, neste caso tem que usar essa função junto com a STR_WORD_COUNT, fazendo a conversão dos caracteres acentuados antes de usar o STRTOLOWER.
        print "<hr><br>"; 

        //STRTOUPPER
        print "Seu nome em maiúsculas é ". strtoupper($nome);//passa tudo para MAIÚSCULO, existe um problema com caracteres acentuados, neste caso tem que usar essa função junto com a STR_WORD_COUNT, fazendo a conversão dos caracteres acentuados antes de usar o STRTOUPPER.
        print "<hr><br>"; 

        //UCFIRST
        print ucfirst("edson gomes dos santos");//passa, apenas, a primeira letra do texto para MAIÚSCULA, existe um problema com caracteres acentuados, neste caso tem que usar essa função junto com a STR_WORD_COUNT, fazendo a conversão dos caracteres acentuados antes
        print "<hr><br>"; 

        //UCWORDS
        print ucwords("edson gomes dos santos");//passa a primeira letra, de cada palavra do texto, para MAIÚSCULA, existe um problema com caracteres acentuados, neste caso tem que usar essa função junto com a STR_WORD_COUNT, fazendo a conversão dos caracteres acentuados antes
        print "<hr><br>"; 

        //STRREV
        print strrev("edson gomes dos santos");//inverte as letras, de trás pra frente, existe um problema com caracteres acentuados, neste caso tem que usar essa função junto com a STR_WORD_COUNT, fazendo a conversão dos caracteres acentuados antes
        print "<hr><br>"; 

        //STRPOS ou STRIPOS
        print strpos("Edson Gomes dos santos", "dos");//posição do "dos" dentro do texto, a contagem começo em "zero". ATENÇÃO é case sensitiv, para resolver isso use a função "stripos"
        print "<hr><br>";
        
        //SUBSTR_COUNT
        print substr_count("Edson Gomes dos Santos Edson Gomes dos Santos Edson...","Edson" );//quantas vezes o nome "Edson" é encontrado no texto.
        print "<hr><br>";

        //SUBSTR
        print substr("Edson Gomes dos  Santos", 4, 8);//pega uma parte do texto, começando em no 4º caractere e pega 8 caracteres à frente. Existe combinações que podem ser feitas com apenas um parâmetro ou com parâmetros negativos, vide abaixo
        print "<hr><br>";
        print substr("Edson Gomes dos  Santos", -4, 2);// dos 4 últimos pega 2
        print "<hr><br>";
        print substr("Edson Gomes dos  Santos", 8);//pega a partir do 8 até o fim
        print "<hr><br>";
        print substr("Edson Gomes dos  Santos",-6);//pega os 6 últimos
        print "<hr><br>";

        //STR_PAD ==> RIGHT, BOTH(ambos) ou LEFT
        $texto = "Gomes";
        $novo = str_pad($texto, 30, "&nbsp", STR_PAD_RIGHT);//insere um texto dentro de outro acrescido e vários "&nbsp" espaços, ou outro caractere até completar 30. OBS: Não funcionou com inserção de espaços, tive que usar o &nbsp que equivale a espaços em html.
        print "Meu professor $novo é muito bom!";
        print "<hr><br>";

        //STR_REPEAT
        $txt = str_repeat("Edson ", 5);//repete o texto 5 vezes, ou quantos quiser.
        print $txt;
        print "<hr><br>";
        print str_repeat("-", 100);
        print "<hr><br>";

        //STR_REPLACE ou STR_IREPLACE
        $frase = "Eu gosto de estudar Matemática";
        print str_ireplace("matemática", "Informática", $frase);//substitui uma palavra por outra dentro de um texto. melhor usar o "str_ireplace que não diferencia maiúsculas de minúsculas. Troca TODAS as palavras caso tenham repetidas. 
    ?>
    <br>
    <img src="" alt="">
</body>
</html>