import './App.css';
import AnotherComponent from './components/AnotherComponent';
import Container from './components/Container';

import FirstComponent from './components/FirstComponent';
import Hooks from './components/Hooks';
import Images from './components/Images';
import List from './components/List';
import RenderCond from './components/RenderCond';

function App() {
  return (
    <div className="App">
      <h2>Hello React</h2>
      <FirstComponent/>
      <AnotherComponent/>
      <Images/>
      <Hooks/>
      <List/>
      <RenderCond x={8} y={10}/>
      <Container>
        <h1>Este é filho do container</h1>
        {/*neste caso pode ser colocado aqui no elemento 'pai', dentro do componente 'Container' outros elementos filhos que serão 'filhos' deste*/}
      </Container>
    </div>
  );
}

export default App;
