import React from "react";
import logo from './componentes/imgs/logo.png'

export default function App(){
    const canal=()=>{
        return('CFB Cursos')
    }
    function curso(){
        return 'Curso de React'
    }
    return (  //O conteúdo abaixo é exportado para index.js
        <> {/*abertura e fechamento do bloco não precisa, necessariamente, de uma tag*/}
        <p>{'Canal: ' + canal()}</p> {/*uma forma de concatenar*/}
        {/*obs.: as tags tem que ter fechamento,senão da erro, ex.: <br/>*/}     
        <p>Curso: {curso()}</p>{/*outra forma de concatenar*/}
        <img src={logo} alt=""></img>
        <img src='/img/Eu.png'/> {/*a tag pode ser fechada assim, ou como na linha acima. Esta imagem tem uma forma diferente de apontamentos pois está no lado do cliente.*/}
        </>
    )
}
//a linha abaixo tb funciona, desde que tire o 'export default' da linha 'export default function App(){'
//export default App