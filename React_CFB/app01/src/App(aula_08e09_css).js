import React from "react";
import Relogio from "./componentes/Relogio";
import './App.css'

export default function App(){  
    const textoDestaque={
        color:'#00f',
        fontSize:'3em'
    }    
    return(
        <>
        <section className="caixa">
          <Relogio/>
          <h1 style={{color:'#f00', fontSize:'5em'}}>CFB Cursos</h1> {/*Atenção: para usar CSS dentro do jsx (inline) separar as propriedades por vírgula e para palavras separadas por hífem deve se usar as palavras sem o hífem, mas a segunda palavra tem que começar com maiúscula. Por ex.: 'font-size fica 'fontSize*/}            
          <h2 style={textoDestaque}>Curso de React</h2>{/*Nesse caso foi feito a mesma coisa da linha acima so que usando uma 'const' previamente definindo as propriedades.*/}
          <p className="texto">Se inscreva em nosso canal e nos siga no instagram</p>{/*Nesse caso o css deriva de um arquivo externo (App.css)*/}
          <a href="#" target='_blank'>CFB Cursos</a>
        </section>
        </>
    )
}