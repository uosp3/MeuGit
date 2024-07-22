import { useState } from 'react';
import SeuNome from './components/SeuNome';
import Saudacao from './components/Saudacao';
import './App.css';

function App() {
  const [nome, setNome] = useState()

  return (
    <div className='App'> 
      <h1>State Lift...</h1>
      <SeuNome setNome={setNome}></SeuNome>
      <Saudacao nome={nome}></Saudacao>
    </div>    
  );
}

export default App;
