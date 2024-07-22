import React, {useState, useEffect} from 'react'
import axios from 'axios'

export default function ListaCarros2(){
    
    const [carros, setCarros]=useState([])
   
    useEffect(()=>{
        axios.get('https://cfbcursosapireactexemplo1.uosp3.repl.co')                   
            .then(res=>{
                const dadosCarros=res.data
                setCarros(dadosCarros)
            })
    })

  
    
    return(
        <div>
            {carros.map(
                carro=> <div key={carro.id}>{carro.id} - {carro.marca} - {carro.modelo}</div>
            )}
        </div>
    )
    
}