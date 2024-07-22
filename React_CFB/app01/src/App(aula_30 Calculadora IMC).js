import React, {useState} from 'react'

const tabelaIMC=()=>{
  return(
    <table border='1' style={{borderCollapse:'collapse'}}>
      <thead>
        <tr>
          <th>
            Classificação
          </th>
          <th>
            IMC
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Abaixo do Peso</td>
          <td>Abaixo de 18,5</td>
        </tr>
        <tr>
          <td>Peso Normal</td>
          <td>Entre 18,5 e 24,9</td>
        </tr>
        <tr>
          <td>Sobrepeso</td>
          <td>Entre 25 e 29,9</td>
        </tr>
        <tr>
          <td>Obesidade Grau I</td>
          <td>Entre 30 e 34,9</td>
        </tr>
        <tr>
          <td>Obesidade Grau II</td>
          <td>Entre 35 e 39,9</td>
        </tr>
        <tr>
          <td>Obesidade Grau III ou Mórbida</td>
          <td>Maior que 40</td>
        </tr>
      </tbody>
    </table>
  )
}

const fpeso=(p,sp)=>{
  return(
    <div>
      <label>Peso 
        {/* (e) = entrada = recebe o componente e sp recebe o valor do componente e passa para o setPeso */}
        <input type={'text'} value={p} onChange={(e)=>{sp(e.target.value)}}></input>
      </label>
    </div>
  )
}

const faltura=(a,sa)=>{ //a=state altura, sa=setAltura
  return(
    <div>
      <label>Altura
         {/* (e) = entrada = recebe o componente e sa recebe o valor do componente e passa para o setAltura */}
        <input type={'text'} value={a} onChange={(e)=>{sa(e.target.value)}}></input>
      </label>
    </div>
  )
}

const fcalular=(p,a,sr)=>{//peso, altura, setResultado  
    const calc=()=>{
      sr(p/(a*a))
    }
  return(
    <div>
      <button onClick={calc}>Calcular</button>
    </div>
  )  
}

const fresultado=(r)=>{
  return( //toFixed(2) para duas casas decimais
    <div>
      <p>Resultado: {r.toFixed(2)}</p>
    </div>
  )
}

export default function App() {

  const [peso, setPeso]=useState(0)
  const [altura, setAltura]=useState(0)
  const [resultado, setResultado]=useState(0)

  return (
    <>
      {fpeso(peso,setPeso)}
      {faltura(altura,setAltura)}
      {fcalular(peso, altura,setResultado)}
      {fresultado(resultado)}
      {tabelaIMC()}
    </>
  );
}