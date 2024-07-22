const { error } = require("console");
const fs = require("fs");
const path = require("path");

//criar uma pasta
fs.mkdir(path.join(__dirname, "/test"), (error) => {
  if (error) {
    return console.log("Erro: ", error);
  }
  console.log("Pasta criada com sucesso");
});

//criar um arquivo
fs.writeFile(
  path.join(__dirname, "/test", "teste.txt"),
  "Arquivo criado pelo arquivo fs.js",
  (error) => {
    if (error) {
      return console.log("Erro ", error);
    }
    console.log("Arquivo criado com sucesso");

    //modificar/adicionar dados ao arquivo
    fs.appendFile(
      path.join(__dirname, "/test", "teste.txt"),
      " Nova informação acrescentada",
      (error) => {
        if (error) {
          return console.log("Erro: " + error);
        }
        console.log("Arquivo modificado com sucesso");
      }
    );
    
    // ler arquivo
    fs.readFile(
      path.join(__dirname, "/test", "teste.txt"),
      "utf8",
      (error, data) => {
        if (error) {
          return console.log("Erro: " + error);
        }
        console.log("Leitura do arquivo: " + data);
      }
    );
  }
);
