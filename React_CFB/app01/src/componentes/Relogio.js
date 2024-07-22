import React from "react";

export default function Relogio(){
    return(        
        <p>
            {new Date().toLocaleTimeString()/*hora em forma de texto, para hora  em formato padrão usar toLocateDateString*/}
        </p>       
        )       
}    