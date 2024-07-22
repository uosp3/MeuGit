
const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://uosp3:M0ng0dbdsqto8@cluster0.sqgcekd.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });
client.connect(err => {
  console.log('aqui')
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
});
/////////////////////////////////////////////////////////////
// Parque MongoDB
// Para desativar este modelo, vá para Configurações | MongoDB | Use o modelo padrão para o playground.
// Certifique-se de estar conectado para habilitar as conclusões e poder executar um playground.
// Use Ctrl+Space dentro de um snippet ou string literal para acionar conclusões.

// Selecione o banco de dados a ser usado.
use('banco');

// O comando drop() destrói todos os dados de uma coleção.
// Certifique-se de executá-lo no banco de dados e na coleção corretos.
db.tabela.drop();

// Inserir alguns documentos na coleção de vendas.
db.tabela.insertMany([
  { '_id': 1, 'item': 'abc', 'price': 10, 'quantity': 2, 'date': new Date('2014-03-01T08:00:00Z') },
  { '_id': 2, 'item': 'jkl', 'price': 20, 'quantity': 1, 'date': new Date('2014-03-01T09:00:00Z') },
  { '_id': 3, 'item': 'xyz', 'price': 5, 'quantity': 10, 'date': new Date('2014-03-15T09:00:00Z') },
  { '_id': 4, 'item': 'xyz', 'price': 5, 'quantity':  20, 'date': new Date('2014-04-04T11:21:39.736Z') },
  { '_id': 5, 'item': 'abc', 'price': 10, 'quantity': 10, 'date': new Date('2014-04-04T21:23:13.331Z') },
  { '_id': 6, 'item': 'def', 'price': 7.5, 'quantity': 5, 'date': new Date('2015-06-04T05:08:13Z') },
  { '_id': 7, 'item': 'def', 'price': 7.5, 'quantity': 10, 'date': new Date('2015-09-10T08:43:00Z') },
  { '_id': 8, 'item': 'abc', 'price': 10, 'quantity': 5, 'date': new Date('2016-02-06T20:20:13Z') },
]);

// Run a find command to view items sold on April 4th, 2014.
db.tabela.find({ date: { $gte: new Date('2014-04-04'), $lt: new Date('2014-04-05') } });

// Execute um comando find para ver os itens vendidos em 4 de abril de 2014.
const aggregation = [
  { $match: { date: { $gte: new Date('2014-01-01'), $lt: new Date('2015-01-01') } } },
  { $group: { _id: '$item', totalSaleAmount: { $sum: { $multiply: [ '$price', '$quantity' ] } } } }
];

// Executa a agregação e abre um cursor para os resultados.
// Use toArray() para esgotar o cursor para retornar todo o conjunto de resultados.
// Você pode usar hasNext()/next() para percorrer o cursor página por página.
db.tabela.aggregate(aggregation);
