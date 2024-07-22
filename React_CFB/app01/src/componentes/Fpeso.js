import React from "react"

export default function Fpeso(props){
    return(
      <div>
        <label>Peso           
          <input type='text' onChange={(e)=>props.setPeso(e.target.value)}></input>                    
        </label>
      </div>
    )
  }