import { useEffect, useState } from "react";
import Topo from "@/components/Topo";
import Globais from "@/components/Globais";

export default function Useeffect(){
    const [cont, setCont]=useState<number>(0)
    const [aux,setAux]=useState<number>(0)

    useEffect(()=>{
        alert('UseEffect disparado')
        Globais.canal="CFBDrone"
        Globais.curso="Typescript"
        Globais.ano="2099"
    },[])

    function add(){
        let a=aux
        a++
        setAux(a)
    }
    
    return(
        <div>
            <Topo/>
            <div>
                <p>{`Valor de cont: ${cont}`}</p>
                <p>{`Valor de aux: ${aux}`}</p>
                <button onClick={add}>Adicionar 1</button>
            </div>
            <div>
                <p>{Globais.canal}</p>
                <p>{Globais.curso}</p>
                <p>{Globais.ano}</p>
            </div>
        </div>
    )
}