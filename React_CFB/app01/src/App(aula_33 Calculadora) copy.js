import React, {useState} from 'react'

export default function App() {

  const [valorTela, setValorTela]=useState('')
  const [resultado, setResultado]=useState(0)
  const [acumulador, setAcumulador]=useState(0)
  const [operado, setOperado]=useState(false)

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
  const addDigitoTela=(d)=>{
    if((d=='+'||d=='-'||d=='*'||d=='/') && operado){
      console.log('+-*/')
      setOperado(false)
      setValorTela(resultado+d)
      return
    }
    if(operado){
      setValorTela(d)
      setOperado(false)
      return
    }
    const valorDigitadoTela=valorTela+d
    setValorTela(valorDigitadoTela)
  }

    const limparMemoria=()=>{
    setOperado(false)
    setValorTela('')
    setResultado(0)
    setAcumulador(0)
    return
  }

  const Operacao=(oper)=>{
    if(oper=='bs'){
      let vtela=valorTela
      vtela=vtela.substring(0, (vtela.length-1))
      setValorTela(vtela)
      setOperado(false)
      return
    }
    
    try{
      const r=eval(valorTela) //cálculo
      setAcumulador(r)
      setResultado(r)
      setOperado(true)
    }catch{
      setResultado('ERRO')
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
        <h3>Calculadora Matemática simples</h3>
        {Tela(valorTela,resultado)}
        <div style={cssBotoes}>
          {Btn('AC', limparMemoria)}
          {Btn('(', ()=>addDigitoTela('('))}
          {Btn(')', ()=>addDigitoTela(')'))}
          {Btn('/', ()=>addDigitoTela('/'))}
          {Btn('7', ()=>addDigitoTela('7'))}
          {Btn('8', ()=>addDigitoTela('8'))}
          {Btn('9', ()=>addDigitoTela('9'))}
          {Btn('*', ()=>addDigitoTela('*'))}
          {Btn('4', ()=>addDigitoTela('4'))}
          {Btn('5', ()=>addDigitoTela('5'))}
          {Btn('6', ()=>addDigitoTela('6'))}
          {Btn('-', ()=>addDigitoTela('-'))}
          {Btn('1', ()=>addDigitoTela('1'))}
          {Btn('2', ()=>addDigitoTela('2'))}
          {Btn('3', ()=>addDigitoTela('3'))}
          {Btn('+', ()=>addDigitoTela('+'))}
          {Btn('0', ()=>addDigitoTela('0'))}
          {Btn('.', ()=>addDigitoTela('.'))}
          {Btn('<-', ()=>Operacao('bs'))}
          {Btn('=', ()=>Operacao('='))}

        </div>
      </div>
    </>
  )
}


