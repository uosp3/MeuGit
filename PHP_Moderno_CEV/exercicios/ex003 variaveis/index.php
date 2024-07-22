<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipos primitivos</title>
</head>
<body>
    <h1>Teste de tipos primitivos</h1>    
    <?php 
    //0x = hexadecimal
    //0b = binário
    // 0 = octal
    // 3e2 = 3 x 10^2

        $num = 0x1a;
        echo "O valor da variável é $num<br>";

        $v = "Edson";
        var_dump($v);//mostra informações sobre a variável
        echo "<br>";
        $num = (int) 3e2;//coerção = o tipo é float mas o (int) faz a conversão para inteiro
        var_dump($num);

        //variável boleano mostra na tela o valor 1 quando TRUE, quando FALSE não mostra nada (vazio)
        echo "<br>";
        $vet = [6, 2.5, "Edson", 3, false];
        var_dump($vet);

        echo "<br>";
        class Pessoa {
            private string $nome;
        }

        $p = new Pessoa;
        var_dump($p);


        echo "<h1>aspas simples ou duplas?</h1>";
        $nome='Edson';
        $sobrenome='Gomes';
        
        echo "$nome $sobrenome <br>";
        echo '$nome $sobrenome';
        echo '<br>Aspas simples não interpreta o conteúdo, apenas exibe tal qual foi digitado';

        echo "<h1>Constantes - Interpolação</h1>";
        echo "Para interpolar constantes ela dever vir concatenada com um 'ponto'<br>";
        const ESTADO = 'MG';
        echo "Eu moro no estado de \u{1F499}" . ESTADO;

        echo "<h1>Sequencia de escape = \+algo</h1>";
        $nom = "Rodrigo";
        $snom = "Nogueira";
        echo "$nom \"Minotauro\" $snom ";//usa a contrabarra para dizer ao php que não quer que ele interprete as aspas como o fechamento da estring
        echo "<br><img src='escape.png' style='width: 300px;'>";

        echo "<h1>Heredoc</h1>";
        $curso = "PHP";
        $ano = date('Y');

        echo <<< FRASE
                    Estou estudando
                        $curso em $ano
            FRASE;
            echo "<br><img src='heredoc.png' style='width: 300px;'>";

        echo "<h1>Nowdoc</h1>";
        $curso = "PHP";
        $ano = date('Y');

        echo <<< 'FRASE'
                    Estou estudando
                        $curso em $ano
            FRASE;
            echo "<br>A diferença para o Heredoc é que a palavra FRASE(apenas a primeira) fica entre aspas simples e consequentemente o php não interpreta as variáveis";

    ?>
</body>
</html>