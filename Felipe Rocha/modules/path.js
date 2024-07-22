const path = require('path')

// Basename
console.log('nome do arquivo que está sendo executado é '+path.basename(__filename)) //nome do arquivo que está sendo executado

//Nome da pasta atual
console.log('A pasta do arquivo atual é '+path.dirname(__filename))
console.log('A pasta do arquivo atual é '+ __dirname) //faz a mesma coisa que a linha acima

//Extensão do arquivo
console.log('A extensão do arquivo atual é '+path.extname(__filename))

//varias informações sobre o arquivo
console.log(path.parse(__filename)) 

//acrescenta mais informações = join
console.log(path.join(__dirname, 'teste', 'teste.html'))

