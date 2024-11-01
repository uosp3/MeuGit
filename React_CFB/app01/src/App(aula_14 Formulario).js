import React, {useState} from "react";

export default function App(){ 
    
    const [nome,setNome]=useState('') 
    const [carro, setCarro]=useState('')     

        return(
        <>
          <label>Digite seu nome</label>
          <input 
              placeholder="Digite seu nome" 
              type='text' 
              nome='fnome' 
              value={nome} 
              onChange={(e)=>setNome(e.target.value)}
          />
          <p>Nome digitado: {nome}</p>

          <label>Selecione um carro</label>
          <select 
              value={carro} 
              onChange={(e)=>setCarro(e.target.value)}>
            <option value='HRV'>HRV</option>
            <option value='Golf'>Golf</option>
            <option value='Cruze'>Cruze</option>
            <option value='Argo'>Argo</option>
          </select>
          <p>Carro selecionado:{carro}</p>
          
        </>
        )};
