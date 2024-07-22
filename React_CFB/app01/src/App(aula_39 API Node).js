import React from "react";
import ListaCarros from "./componentes/ListaCarros_ComponentesClasse";
import ListaCarros2 from "./componentes/ListaCarros_ComponenteFuncional";
import ListaCarros3 from "./componentes/ListaCarros_FETCH";

export default function App(){
    return(
        <>  
            <h1>Componentes de classe</h1>
            <ListaCarros></ListaCarros>
            <h1>Componentes funcional</h1>
            <ListaCarros2></ListaCarros2>
            <h1>Com FETCH</h1>
            <ListaCarros3></ListaCarros3>
        </>
    )
}