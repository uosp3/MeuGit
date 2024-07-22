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
            require_once 'Pessoa.php';
            require_once 'Livro.php';
            $ps[0] = new Pessoa("Pedro", 22, "M");
            $ps[1] = new Pessoa("Maria", 31, "F");
            $l[0] = new Livro("PHP Básico", "Jose da Silva", 300, $ps[0]);
            $l[1] = new Livro("POO com PHP", "Maria de Souza", 500, $ps[0]);
            $l[2] = new Livro("PHP Avançado", "Ana Paula", 800, $ps[1]);

            $l[0]->abrir();
            $l[0]->folhear(300);
            $l[0]->avancarPag();
            $l[0]->detalhes();
            $l[1]->detalhes();
            $l[2]->detalhes();

            //print_r($l[0]);
        ?>
    </pre>
</body>
</html>