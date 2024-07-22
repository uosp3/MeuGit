import React,{useState} from "react";
import Numero from "./componentes/Numero";
import './App.css'

export default function App(){

    const [num, setNum]=useState(10)
    const [nome, setNome]=useState('Edson')

    return(
        <>
            <p>Valor de state num em App: {num}</p>  
            <Numero num={num} setNum={setNum}/>
            <p>{nome}</p>                    
        </>
    )
}