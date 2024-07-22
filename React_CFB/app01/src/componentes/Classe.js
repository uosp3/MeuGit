import React from "react";

export default class Classe extends React.Component{
    constructor(props){
        super(props) //chama o construtor da classe pai 'React.Component'
    }
    render(){
        return(
            <div>
                <h1>Primeiro Componente de Classe</h1>
                <p>Canal: {this.props.canal/*para comp de class tem que usar o this */}</p>
                <p>Curso: {this.props.curso}</p>
            </div>
        )
    }
}