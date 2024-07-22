import { useState } from "react"
function Condicional(){

    const [email, setEmail] = useState()
    const [userEmail, setUserEmail] = useState()

    function enviarEmail(e){
        e.preventDefault() //inibe o envio do form, para teste.
        setUserEmail(email)        
    }

    function limparEmail(){
        const mala=document.getElementById('mala')        
        mala.value=''
        setUserEmail('')
    }

    return(
        <div>
            <h2>Cadastre o seu e-mail:</h2>
            <form>
                <input 
                id="mala" 
                type="email" 
                placeholder="Digite o seu e-mail..." 
                onChange={(e)=> setEmail(e.target.value)}/>
                <button type="submit" onClick={enviarEmail}>Eviar e-mail</button>
                {userEmail && ( //funciona como um 'if'
                    <div>
                        <p>O e-mail do usuário é: {userEmail}</p>
                        <button onClick={limparEmail}>Limpar</button>
                    </div>
                )}
            </form>
        </div>    
    )

}
export default Condicional