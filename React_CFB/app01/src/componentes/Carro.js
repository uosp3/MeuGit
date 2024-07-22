import React from "react";

export default class Carro extends React.Component{
    constructor(props){
        super(props) //chama o construtor da classe pai 'React.Component'
        this.modelo='Golf'
        this.state={
            ligado:false,
            velAtual:0,
        }
    }
    ligarDesligar(){
        //this.state.ligado=true ===== não da erro, mas não atualiza a tela
        //this.setState({ligado:!this.state.ligado})   = forma abaixo é mais segura
        this.setState(
            (state)=>(
                {ligado:!state.ligado,
                velAtual:0}
                )
        )
    }

    acelerar(){
        if(this.state.ligado){
        this.setState(
            (state, props)=>(
                {velAtual:state.velAtual + props.fator}
            )
        )}else{
            alert('Ligue o carro')
        }
    }

    render(){
        return(
            <div>
                <h1>Meu Carro</h1>
                <p>Modelo: {this.modelo}</p>
                <p>Ligado: {this.state.ligado ? 'Sim': 'Não'}</p> 
                <p>Velocidade: {this.state.velAtual}</p>  
                <button onClick={()=>this.ligarDesligar()}>
                    {this.state.ligado ? 'Desligar Carro':'Ligar Carro'}
                </button>  
                <button onClick={()=>this.acelerar()}>
                    Acelerar
                </button>               
            </div>
        )
    }
}