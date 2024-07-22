<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 02 - POO</title>
</head>
<body>
    
        <pre>
            <?php
               require_once 'Caneta.php'; // carrega o arquivo
                $c1 = new Caneta;
                $c1 -> modelo = "BIC Cristal";
                $c1 -> cor = "Azul";
                //$c1 -> ponta = 0.5;  ===== privado, não posso alterar
                //$c1 -> carga = 99;   ===== protegido, não posso alterar
                print_r($c1);
                $c1 -> rabiscar();

                $c1 -> tampar(); // atributo 'tampada' está protegido mas a função (método 'tampar') tem acesso e pode alterar
                print "<hr>";
                print_r($c1);
            ?>

        </pre>
    
</body>
</html>