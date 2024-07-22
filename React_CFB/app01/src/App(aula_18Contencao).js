import React, { useState } from "react";
import Caixa from "./componentes/Caixa";
import Canal from "./componentes/Canal";


export default function App(){

  return(
    <>
    <Caixa site="www.cfbcursos.com.br =  gerado aqui e levado para 'Caixa'">
      <Canal></Canal>      
      <p>Curso de React</p>
    </Caixa>
    </>
  )
}
