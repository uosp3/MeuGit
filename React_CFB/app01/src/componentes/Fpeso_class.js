import React from "react"

export default class Fpeso extends React.Component{
  constructor(){ //necessário para trabalhar com props
    super()
  }
  render(){
    return(
      <div>
        <label>Peso           
          <input type='text' onChange={(e)=>this.props.setPeso(e.target.value)}></input>                    
        </label>
      </div>
    )
  }
}