import './App.css';
//import HelloWorld from './components/HelloWorld';
import Frase from './components/Frase';
import SayMayName from './components/SayMayNome';
import Pessoa from './components/Pessoa';
import List from './components/List';

function App() {
  const nome='Gomes'
  return (
    <div className='App'> 
      <Frase></Frase>     
      <SayMayName nome='Edson'></SayMayName>  
      <SayMayName nome={nome}></SayMayName>  
      <Pessoa
        nome='Edson'
        idade='61'
        profissao='Programador'
        foto='https://via.placeholder.com/150'
      >        
      </Pessoa>
      <List></List>
    </div>    
  );
}

export default App;
