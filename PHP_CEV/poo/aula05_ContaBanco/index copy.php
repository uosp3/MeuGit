<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <pre>
        <?php
            require_once 'ContaBanco.php';
        
            $c1 = new ContaBanco(); 

            $c1 -> abriConta("CP");            
            print_r($c1);            
            
            print "<hr>Para fechar a conta<br>";            
            $c1 -> fecharConta();
            print_r($c1);

            print "<hr>Fazendo deposito<br>";            
            $c1 -> depositar(25);
            print_r($c1);

            print "<hr>Fazendo saque<br>";            
            $c1 -> sacar(95);
            print_r($c1);

            print "<hr>Pagando tarifa da conta<br>";            
            $c1 -> pagarMensal();
            print_r($c1);
        ?>
    </pre>
    
</body>
</html>