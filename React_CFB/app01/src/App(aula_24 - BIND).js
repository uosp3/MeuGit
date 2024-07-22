import React from "react";
import Classe from "./componentes/Classe";
import Carro from "./componentes/Carro_BIND";

export default function App(){  

    return(
    <>
      <h1>Componentes de Classe.</h1>
      <Classe canal='CFB Curso' curso='React'></Classe>
      <Carro fator={1}></Carro>
    </>
    )
};