import React, {useState} from "react";
import Led from './componentes/Led'
export default function App(){   
    
    const [ligado, setLigado]=useState(false)

    const cancelar=(obj)=>{
        return obj.preventDefault()//cancela a ação do click no link
    }

    return(
        <>  
          <Led ligado={ligado} setLigado={setLigado}/> 
          <a 
            href="http://youtube.com/cfbcursos"
            target='_blanck'
            onClick={(e)=>cancelar(e)}            
            >           
                CFB Cursos
          </a>    
        </>
    )
}