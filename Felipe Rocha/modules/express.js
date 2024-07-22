const express = require("express");
const UserModel = require("../src/models/user.model");

const app = express();

app.use(express.json());

app.get("/users", async (req, res) => {
  //get para pegar e post para criar
  try {
    const users = await UserModel.find({}); //pega todos os usuários

    res.status(200).json(users);
  } catch (error) {
    return res.status(500).send(error.message);
  }
});

app.get("/users/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const user = await UserModel.findById(id); //pega apenas um usuário
    return res.status(200).json(user);
  } catch (error0) {
    return res.status(500).send(error.message);
  }
});

app.post("/users", async (req, res) => {
  try {
    const user = await UserModel.create(req.body);

    res.status(201).json(user); //201 = registro criado com sucesso
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.patch("/users/:id", async (req, res) => {
  try {
    const id = req.params.id;
    const user = await UserModel.findByIdAndUpdate(id, req.body, { new: true }); //{new: true} para retornar o registro ja atualizado.
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.delete('/users/:id', async(req,res)=>{
  try{
    const id=req.params.id
    const user=await UserModel.findByIdAndRemove(id)
    res.status(200).json(user)
  } catch (error){
    res.status(500).send(error.message)
  }
})
const port = 8080;

app.listen(port, () => console.log(`Rodando com express na porta ${port}`));
