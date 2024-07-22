import React from "react"

export default function Fresultado(props){
    return(
      <div>
        <p>Resultado: {Number(props.resultado).toFixed(2)}</p>
      </div>
    )
  }