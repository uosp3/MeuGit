import React, { useEffect, useState } from "react"
export default function App(){

  const [contagem, setContagem]=useState(0)

  useEffect(/*é executado sempre que a pag é carregado e quando houver uma att */
    ()=>{
      console.log('Página carregada')
      document.title='Contagem: '+ contagem
    }
  )

  return(
    <>
      <p>Contagem: {contagem}</p>
      <button onClick={()=>setContagem(contagem+1)}>Contar</button>
    </>
  );
}