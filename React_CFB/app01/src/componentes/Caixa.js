import React from "react";

export default function Caixa(props){
    return(
        <>
            <p>{props.site /*passado pelo App*/}</p>
            {props.children}
            {/*props.children[0]/*pode ser como array*/}
        </>
    )
}
