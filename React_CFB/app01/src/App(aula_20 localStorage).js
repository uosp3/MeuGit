import React, { useState } from "react"
export default function App(){ 
/* GRAVAR DADOS NO NAVEGADOR, F12+'aplication' para ver o resultado.
  localStorage.setItem('nome', 'Edson')//chave 'nome' de valor 'Edson'
  localStorage.getItem('nome') //obter o valor da chave
  localStorage.removeItem('nome')//remove a chave
*/
const [nome, setNome]=useState()

const armazenar=(chave, valor)=>{
  localStorage.setItem(chave, valor)
}

const consultar=(chave)=>{
  alert(localStorage.getItem(chave))
}

const apagar=(chave)=>{
  localStorage.removeItem(chave)
}
  
  return(
    <>
      <label>Digite um nome: </label><br/>
      <input type='text' value={nome} onChange={(e)=>setNome(e.target.value)}></input><br/>
      <button onClick={()=>armazenar('ls_nome', nome)}>Gravar nome</button>
      <button onClick={()=>consultar('ls_nome')}>Ver nome</button>
      <button onClick={()=>apagar('ls_nome')}>Remover nome</button>
    </>
  );
}