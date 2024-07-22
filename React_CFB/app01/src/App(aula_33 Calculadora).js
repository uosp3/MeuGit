/*Fiz o desafio e conto com a ajuda dos demais para verificar se está ok ou se ficou algum bug.
Fiz com os seguintes casos:
1 - Não permite operações em sequencia, nem ponto em sequencia.
2 - Não permite mais de um ponto por sequencia de números digitados, antes que se coloque um outro operador.
3 - Não permite fechar parênteses sem que tenha sido aberto.
4 - Não permite fechar mais parênteses do que o tanto que foi aberto.
5 - Não permite iniciar com um sinal de vezes ou dividir, antes de qualquer número.
6 - Se esquecer de fechar algum parêntese o sistema fecha antes de fazer o cálculo final
7 - Não permite operação de multiplicação e divisão se não for depois de um número ou de um parêntese fechado
8 - Se abrir parêntese depois de um número, sem colocar uma operação o sistema coloca a operação de multiplicação
9 - So permite colocar ponto após um número.
Acho que é tudo, fiz alguns teste mas pode ser que tenha ficado algo mais para acertar. Caso alguém se interesse segue o código completo:*/

import React, {useState, useEffect} from 'react'

export default function App() {

  const [valorTela, setValorTela]=useState('')
  const [resultado, setResultado]=useState(0)
  const [ultimoDigito, setUltimoDigito]=useState('')
  const [ponto, setPonto]=useState('S')
 

  //COMPONENTES   
  const Tela=(valor,res)=>{
    return(
      <div style={cssTela}>
        <span style={cssTelaOper}>{valor}</span>
        <span style={cssTelaRes}>{res}</span>
      </div>
    )
  }
  const Btn=(label, onClick)=>{    
    return(
      <button style={cssBtn} onClick={onClick}>{label}</button>
    )
    
  }

    //FUNÇÕES
  const addSinalTela=(s)=>{             
      switch(s){       
        case '/':
        case '*':          
            if(Number(ultimoDigito)||ultimoDigito==')'){  //so aceita multiplicação e divisão se o último digito for um número ou um parentese fechado.            
              setValorTela(valorTela+s) 
              setUltimoDigito(s)
              setPonto('S')  
            }            
          break

        case '+':
        case '-':
          if(Number(ultimoDigito)||(ultimoDigito=='(')||(ultimoDigito==')')){
            setValorTela(valorTela+s)
          }else{          
            setValorTela(valorTela.substring(0,(valorTela.length-1))+s)                
          }
          setUltimoDigito(s)     
          setPonto('S')   
          break

        default:
            alert('Erro não previsto!')
      }
  }

  const addParentesesTela=(par)=>{               
    if(par=='('){
      if(Number(ultimoDigito)||ultimoDigito==')'){ //se for abrir um parentese ao lado de um número, sem o sinal '+, -, *, /,' ou ao lado de um parentesese fechado. Coloca o sinal de multiplicar antes de inserir o parentese
        setValorTela(valorTela+'*'+par)
        setUltimoDigito(par)
        setPonto('S')         
      }else{         
        if(ultimoDigito!=='.'){ //abre o parentese se o último dígito for diferente de ponto
        setValorTela(valorTela+par)
        setUltimoDigito(par)
        setPonto('S')
        }
      }            
    } 

    let abertos=valorTela.split('').filter((letra)=> letra.indexOf('(') !== -1)
    let fechados=valorTela.split('').filter((letra)=> letra.indexOf(')') !== -1)

    if(abertos.length>fechados.length){//so permite fechar, no máximo, a quantidade de parenteses que tiver abertos
      if(par==')'){      
        if(Number(ultimoDigito)||ultimoDigito==')'){ 
          setValorTela(valorTela+par)
          setUltimoDigito(par)   
        }
      }   
    }         
  }

  const addPontoTela=(p)=>{ //so permite colocar ponto se setPonto for 'S' e se ultimo dígito for mumero. 
    //alert('Ponto '+ ponto) 
   //alert('Ultimo ' + Number(ultimoDigito + 1))       
      if((Number(ultimoDigito) || ultimoDigito==0) && ponto=='S'){//o sistema não considerou zero como número! ????
      setValorTela(valorTela+p)
      setUltimoDigito(p)
      setPonto('N')    
    }
      if(valorTela==''){
        setValorTela(0.+p)
        setUltimoDigito(p)
        setPonto('N')
      }
      if(ultimoDigito=='-'||ultimoDigito=='+'||ultimoDigito=='*'||ultimoDigito=='/'||ultimoDigito=='('){      
        setValorTela(valorTela+0+p)
        setUltimoDigito(p)
        setPonto('N')
      }
      if(ultimoDigito==')'){
        setValorTela(valorTela+'*'+0+p)
        setUltimoDigito(p)
        setPonto('N')
      }     
  }
   
  const addDigitoTela=(d)=>{               
    if(valorTela==''){
      setValorTela(d)
    }else{
      if(ultimoDigito==')'){
        setValorTela(valorTela+'*'+d)
      }else{ 
        setValorTela(valorTela+d)
      }
    }      
  setUltimoDigito(d)  
  }

  const limparMemoria=()=>{    
    setValorTela('')
    setUltimoDigito('') 
    setResultado(0)    
    setPonto('S')
    return
  }
   
  const Operacao=(oper)=>{    
    if(oper=='bs'){
      let vtela=valorTela           
        let vaiApagar=vtela.substring(vtela.length-1, vtela.length)  //caractere que será apagado               
        
          //verifica, de traz pra frente, os próximos caracteres. Se achar um ponto, antes de achar um sinal ('+, -, *, /, ou parentesese') sai do loop sem permitir inserir ponto.
          for(let i=vtela.length-1;i>0;i--){
              let lido=vtela.substring(i,i-1)              
              if (lido=='.'){
                setPonto('N')                  
                break
              }              
              //caso não encontre um ponto antes do próximo sinal '+, -, *, /, ou parentesese' permite inserir ponto e sai do loop              
                if(!Number(lido)){
                setPonto('S')
                break
              }
          }         
        //}  
        if(vaiApagar=='.'){setPonto('S') }           
        vtela=vtela.substring(0, (vtela.length-1))
        setUltimoDigito(vtela.substring(vtela.length-1, vtela.length))                      
        setValorTela(vtela)   //refaz o valor da tela sem o último caractere           
      return
    }
    
      let abertos=valorTela.split('').filter((letra)=> letra.indexOf('(') !== -1) //parenteses abertos
      let fechados=valorTela.split('').filter((letra)=> letra.indexOf(')') !== -1) //parenteses fechados

      //antes de tentar fazer o cálculo verifica se todos os parenteses foram fechados.
      if(abertos.length>fechados.length){
        alert('Voce esqueceu de fechar algum parêntese, o sistema fará a correção automática caso voce concorde com a correção clique novamente no = para efetuar o cálculo.')
        setUltimoDigito(')')   
        let acerta=''
        let faltaParenteses=(abertos.length-fechados.length)       
        for(let i=0;i<faltaParenteses;i++){                
          acerta=(acerta+')')          
         }               
          setValorTela(valorTela+acerta) //fecha os parenteses que estão faltando.                     
        }else{
        try{                                          
          const r=eval(valorTela) //cálculo      
          setResultado(r.toFixed(2))                 
        }catch{                
          setResultado('ERRO')       
        }
       }             
  }
  
  //ESTILOS
  const cssContainer={
    display:'flex',
    justifyContent:'flex-start',
    alignItens:'center',
    flexDirection:'column',
    width:300,
    border: '1px solid #000'
  }
  const cssBotoes={
    flexDirection:'row',
    flexWrap:'wrap'
  }

  const cssTela={
    display: 'flex',
    paddingLeft: 20,
    paddingRight: 20,
    justifyContent: 'center',
    alignItens: 'flex-start',
    backgroundColor: '#444',
    flexDirection:'column',
    width:260
  }
  const cssTelaOper={
    fontSize:25,
    color:'#fff',
    height:20    
  }
  const cssTelaRes={
    fontSize:50,
    color: '#fff'
  }
  const cssBtn={
    fontSize:30,
    height:75,
    width:75,
    padding:20,
    backgroundColor:'#000',
    color:'#fff',
    borderColor:'#000',
    textAlign: 'center',
    outline:'none'
  }

  return(
    <>
      <div style={cssContainer}>
      <h3>Calculadora Matemática Simples</h3>
        {Tela(valorTela,resultado)}
        <div style={cssBotoes}>
          {Btn('Del', limparMemoria)}
          {Btn('(', ()=>addParentesesTela('('))}
          {Btn(')', ()=>addParentesesTela(')'))}
          {Btn('/', ()=>addSinalTela('/'))}
          {Btn('7', ()=>addDigitoTela('7'))}
          {Btn('8', ()=>addDigitoTela('8'))}
          {Btn('9', ()=>addDigitoTela('9'))}
          {Btn('*', ()=>addSinalTela('*'))}
          {Btn('4', ()=>addDigitoTela('4'))}
          {Btn('5', ()=>addDigitoTela('5'))}
          {Btn('6', ()=>addDigitoTela('6'))}
          {Btn('-', ()=>addSinalTela('-'))}
          {Btn('1', ()=>addDigitoTela('1'))}
          {Btn('2', ()=>addDigitoTela('2'))}
          {Btn('3', ()=>addDigitoTela('3'))}
          {Btn('+', ()=>addSinalTela('+'))}
          {Btn('0', ()=>addDigitoTela('0'))}
          {Btn('.', ()=>addPontoTela('.'))}
          {Btn('<-', ()=>Operacao('bs'))}
          {Btn('=', ()=>Operacao('='))}
        </div>        
      </div>
    </>
  )
}