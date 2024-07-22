import React from 'react'
import Dados from './Dados'

export default function Corpo(){
    const cnl = "CFB Cursos"
  return (
    <section>
       <h2>Curos de React</h2> 
       <p>Se inscreva em nosso canal</p>
       <Dados  
          canal={cnl} 
          youtube='youtube.com/cfbcursos' 
          curso='React.js'/>    
    </section>
  )
}

