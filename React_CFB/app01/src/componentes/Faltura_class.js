import React from "react"

export default class Faltura extends React.Component {
  constructor(){
    super()
  }
  render(){
    return(
      <div>
        <label>Altura           
          <input type='text' onChange={(e)=>{this.props.setAltura(e.target.value)}}></input>
        </label>
      </div>
    )
  }
}