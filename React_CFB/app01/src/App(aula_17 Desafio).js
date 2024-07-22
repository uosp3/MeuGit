import React, { useState } from "react";

//import Resultado from './componentes/Resultado'
function Resultado(props){
  return(
      <div>
          <p>Soma das notas: {props.somaNotas}</p>
          <p>{props.somaNotas >= 60 ? 'Aprovado' : 'Reprovado'}</p>            
      </div>
  )
}

//import Nota from './componentes/Nota'
function Nota(props){
  return(
      <div>
          <legend>Informe a nota: {props.num}</legend>
          <input type='text' name={props.nome} onChange={(e)=>props.setNota(e)}></input>            
      </div>
  )
}

export default function App(){

  const [notas,setNotas]=useState({'nota1':'0', 'nota2':'0', 'nota3':'0', 'nota4':'0'})
  /*ALTERNATIVA FEITA PELO PROFESSOR ===================
  const handleSetNotas=(e)=>{
    if(e.target.getAttribute('name')=='nota1'){      
      setNotas({'nota1':e.target.value, 'nota2':notas.nota2, 'nota3':notas.nota3, 'nota4':notas.nota4})
    } else if(e.target.getAttribute('name')=='nota2'){
      setNotas({'nota1':notas.nota1, 'nota2':e.target.value, 'nota3':notas.nota3, 'nota4':notas.nota4})
    } else if(e.target.getAttribute('name')=='nota3'){
      setNotas({'nota1':notas.nota1, 'nota2':notas.nota2, 'nota3':e.target.value, 'nota4':notas.nota4})
    } else if(e.target.getAttribute('name')=='nota4'){
      setNotas({'nota1':notas.nota1, 'nota2':notas.nota2, 'nota3':notas.nota3, 'nota4':e.target.value})
    }
  }*/

  //ALTERNATIVA PASSADA NOS COMENTÁRIOS DO VÍDEO ============
  const handleSetNotas=(e)=>{
    let novoEstado = {...notas}
    novoEstado[e.target.getAttribute('name')] = e.target.value   
    console.log(novoEstado)
    setNotas(novoEstado);
  }



  return(
    <>
    <Nota nome={'nota1'} num={1} nota={notas.nota1} setNota={handleSetNotas}/>
    <Nota nome={'nota2'} num={2} nota={notas.nota2} setNota={handleSetNotas}/>
    <Nota nome={'nota3'} num={3} nota={notas.nota3} setNota={handleSetNotas}/>
    <Nota nome={'nota4'} num={4} nota={notas.nota4} setNota={handleSetNotas}/>
    <Resultado somaNotas={parseFloat(notas.nota1)+parseFloat(notas.nota2)+parseFloat(notas.nota3)+parseFloat(notas.nota4)}/>
    </>
  )
}
