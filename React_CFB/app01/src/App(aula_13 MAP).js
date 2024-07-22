import React from "react";

export default function App(){    
    
    const carros=[//json
        {categoria: 'Esporte', preco:'110.000.00', modelo:'Golf GTI'},
        {categoria: 'Esporte', preco:'120.000.00', modelo:'Camaro'},
        {categoria: 'SUV', preco:'85.000.00', modelo:'HRV'},
        {categoria: 'SUV', preco:'83.000.00', modelo:'T-Cross'},
        {categoria: 'Utilitári', preco:'120.000.00', modelo:'Hillux'},
        {categoria: 'Utilitário', preco:'90.000.00', modelo:'Ranger'}
    ];

    const listaCarros=carros.map(
        (c,i)=>
        <li>{i} - {c.categoria} - {c.modelo} - R${c.preco}</li>
    )

        return(
        <>
          <ul>{listaCarros}</ul>         
        </>
        )
}