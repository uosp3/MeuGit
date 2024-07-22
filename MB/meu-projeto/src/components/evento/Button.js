function Button(props){
    return( //sendo apenas uma linha(abaixo) os parênteses são facultativos, mas linha ficaria em frente ao return
        <button onClick={props.event}>{props.text}</button>
    )    
}
export default Button