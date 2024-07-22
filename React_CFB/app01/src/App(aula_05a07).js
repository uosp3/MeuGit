import React from "react";
import Header from './componentes/Header'
import Corpo from "./componentes/Corpo";


export default function App(){      
    return (  
        <>
            <Header/>
            <Corpo/>{/*tem outro elemento (Dados) dentro deste*/}            
        </>
    )
}