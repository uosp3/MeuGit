import React from "react";
import Dados from "./Dados";

export default function Corpo(){
    const cnl=()=>{
        return 'CFB Cursos'
    }
    const somar=(v1,v2)=>{
        return v1+v2
    }
    const yt='youtube.com/cfbcursos'  
    return(
        <section>
            <h2>Curso de React</h2>
            <p>Se inscreva em nosso canal</p>
            <p>Ative o sininho e clique no joinha</p>
            <Dados //esse é um elemento 'Dados' dentro do outro 'Corpo'
                canal={cnl}//pode ser feito atribuindo a string a uma 'function'     
                youtube={yt}//pode ser feito atribuindo a string a uma 'const'                
                curso='React.js'
                somar={somar}/>
        </section>
    )
}