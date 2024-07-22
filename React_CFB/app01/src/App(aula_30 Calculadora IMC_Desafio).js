import React, {useState} from 'react'
//os imports abaixo foram alterados para que o app funcione de duas formas, com componentes com funções e com class. Os arquivos tem os mesmos nome, exceto pela palavra _class no final do nome. Se tirar o _class tem que funcionar do mesmo jeito.
import TabelaIMC from './componentes/TabelaIMC_class'
import Fpeso from './componentes/Fpeso_class'
import Faltura from './componentes/Faltura_class'
import Fcalcular from './componentes/Fcalcular_class'
import Fresultado from './componentes/Fresultado_class'

export default function App() {

  const [peso, setPeso]=useState(0)
  const [altura, setAltura]=useState(0)
  const [resultado, setResultado]=useState(0)

  return (
    <>      
      <Fpeso setPeso={setPeso} ></Fpeso>      
      <Faltura setAltura={setAltura}></Faltura>      
      <Fcalcular setResultado={setResultado} p={peso} a={altura}></Fcalcular>      
      <Fresultado resultado={resultado}></Fresultado>
      <TabelaIMC></TabelaIMC>
    </>
  );
}