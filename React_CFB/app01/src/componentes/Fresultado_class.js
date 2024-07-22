import React from "react"

export default class Fresultad extends React.Component {
  constructor(){
    super()
  }
  render(){
    return(
      <div>
        <p>Resultado: {Number(this.props.resultado).toFixed(2)}</p>
      </div>
    )
  }
}