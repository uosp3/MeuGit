import React from "react"

export default function Faltura(props){
    return(
      <div>
        <label>Altura           
          <input type='text' onChange={(e)=>{props.setAltura(e.target.value)}}></input>
        </label>
      </div>
    )
  }