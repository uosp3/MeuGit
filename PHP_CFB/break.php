<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comando BREAK</title>
</head>
<body>
    <?php
        $vet=array("mouse", "teclado", "monitor", "memória", "sair", "microfone", "impressora");
        $tam=count($vet);
        $i=0;

        while ($i<$tam) {
            print "$vet[$i] i = $i<br>";
            $i++; //incrementa antes de verificar a próxima passagem pelo loop
            if ($vet[$i] == "sair") {
                break;
            }
        }

        print "<hr>";

        for ($i=0; $i<$tam; $i++){ //incrementa depois da próxima passagem pelo loop            
            if ($vet[$i] == "sair") {
                break;
            }
            print "$vet[$i] i = $i<br>";
        }

        print "<hr>";

        foreach ($vet as $pc){             
            if ($pc == "sair") {
                break;
            }
            print "$pc<br>";
        }

    
    ?>
</body>
</html>