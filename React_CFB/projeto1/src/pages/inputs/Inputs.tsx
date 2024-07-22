import { useState, useEffect } from "react"
import Topo from "@/components/Topo"
import Globais from "@/components/Globais"

const cursos=["HTML","React","C++","Javascript","Arduino","CSS"]
const jcursos=[//tb pode ser usado um objeto json, vide comentários abaixo.
    {"Curso":"HTML"},
    {"Curso":"React"},
    {"Curso":"C++"},
    {"Curso":"Javascript"},
    {"Curso":"Arduino"},
    {"Curso":"CSS"}
]

export default function Inputs(){
    const [nome, setNome]=useState<string>("")
    const [curso, setCurso]=useState<string>(cursos[0])

    useEffect(()=>{
        Globais.curso="React"
    },[])

    function fcursos(){
        return cursos.map((c:any)=>{
            return <option value={c} key={Math.random()*99999999999999999}>{`Curso de ${c}`}</option>
        })
    }
//a constante abaixo faz o mesmo que a função acima.
    const ccursos=cursos.map((c:any)=>{//para usar o json troca cursos.map por jcursos.map
        return <option value={c.curso} key={Math.random()*99999999999999999}>{`Curso de ${c.curso}`}</option>//para json usa c.curso
    })

    return(
        <div>
            <Topo/>
            <div className="campoForm">
                <label>Nome</label>
                <input type="text" value={nome} onChange={(evt)=>setNome(evt.target.value)}/>
            </div>
            <div className="campoForm">
                <label>Curso</label>
                <select value={curso} onChange={(evt)=>setCurso(evt.target.value)}>
                    {
                        fcursos() //aqui pode ser usado tanto a função quando a constante ccursos.
                        //ccursos
                    }
                </select>
            </div>
            <div>Nome digitado: {nome}</div>
            <div>Curso escolhido: {curso}</div>
            <div>
                <p>{Globais.canal}</p>
                <p>{Globais.curso}</p>
                <p>{Globais.ano}</p>
            </div>
        </div>
    )
}