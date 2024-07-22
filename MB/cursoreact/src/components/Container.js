//neste caso pode ser colocado no elemento 'pai', dentro do compoente 'Container' outros elementos filhos que serão 'filhos' deste. Vide 'children' na props 
const Container =({children})=>{
    return <div>{children}</div>
}

export default Container