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
    <h1>Números primos</h1>        
        <?php
            $num = $_GET["num"];
            $multiplos = 0;
            print "<h2>Analisando o número $num</h2>";        
            print "Valores múltiplos: ";
            for ($p = 1; $p<=$num; $p++){
                   if ($num%$p == 0){
                    print "$p, ";
                    $multiplos++;
                }
            }
            print "<br>Total de múltimplos: $multiplos<br>";
            
            if ($multiplos==2){
                print "Resultado: $num É PRIMO";
            }else{
                print "Resultado: $num NÃO É PRIMO";
            }         
        ?>       
    <br><br> <a href="02index.html">Voltar</a>
    
</body>
</html>