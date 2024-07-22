import React from "react";

function ListaNumeros(props){
    const num=props.numeros
    const lista_numeros=num.map(
        (n)=> //retornando apenas um elemento não é necessário {}
            <li key={n.toString()}>{n}</li> //usar o key sempre que estiver retornando uma lista de elementos. O react usa para saber qual elemento operar (iterar?)
    )
    return(<ul>{lista_numeros}</ul>)
}

const array_numeros=[1,2,3,4,5,6,7,8,9]

export default function App(){
    return(
        <>
            <ListaNumeros numeros={array_numeros}></ListaNumeros>
        </>
    )
}