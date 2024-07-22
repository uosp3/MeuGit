import React, {useState} from "react";

export default function App(){ 
    
    const [form,setForm]=useState({'nome':'', 'curso':'', 'ano':''}) 
    const handlFormChange=(e)=>{
      if(e.target.getAttribute('name')=='fnome'){
        setForm({'nome':e.target.value, 'curso':form.curso, 'ano':form.ano})
      }else if(e.target.getAttribute('name')=='fcurso'){
        setForm({'nome':form.nome, 'curso':e.target.value, 'ano':form.ano})
      }else if(e.target.getAttribute('name')=='fano'){
        setForm({'nome':form.nome, 'curso':form.curso, 'ano':e.target.value})
      }    
    }  

        return(
        <>
          <label>Nome</label>
          <input type='text' name='fnome' onChange={(e)=>handlFormChange(e)}/><br/>
          <label>Curso</label>
          <input type='text' name='fcurso' onChange={(e)=>handlFormChange(e)}/><br/>
          <label>Ano</label>
          <input type='text' name='fano' onChange={(e)=>handlFormChange(e)}/><br/>

          <p>Nome digitado:{form.nome}</p>
          <p>Curso digitado:{form.curso}</p>
          <p>Ano digitado:{form.ano}</p>
        </>
        )};
