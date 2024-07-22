import React from "react"

export default class Fcalcular extends React.Component {
  constructor(){
    super()
    //this.calc=this.fcalc.bind(this) //== o prof usou o BIND mas não foi necessário.
  }
  calc=()=>{ //usando o BIND aqui seria fcalc
    const r=this.props.p/(this.props.a*this.props.a)  
    this.props.setResultado(r) 
           
  }
  render(){
    return(
        <div>
          <button onClick={this.calc}>Calcular</button>
        </div>
      )  
    }
}