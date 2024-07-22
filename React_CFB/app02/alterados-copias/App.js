import React from "react";
import Logo from './componentes/imgs/logo.png'
import Eu from './componentes/imgs/eu.png'

export default function App(){
  const canal=()=>{
    return("CFB Cursos")
  }
  const curso = "Curso de React";
  return(
    <section>
    <header>
      {/* pode concatenar de duas formas: */}
        <p>Canal: {canal()}</p>
        <p>{'Curso: ' + curso}</p>
    </header>
      <div>
        <img src={Logo} alt="Logomarca"/>
        {/* abaixo exemplo de imagem for do servidor, diretamente em public */}
        <img src="/img/eu.png"/>
      </div>
    </section>
  )
}