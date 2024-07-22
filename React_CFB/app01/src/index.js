import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App(aula_12 Renderizacao condicional2)';//importa o './App' e atribui lhe o nome de App
import reportWebVitals from './reportWebVitals';

//linhas 9, 17 e 18 foram comentadas pois estava dando 'tilt' no console na aula 19
//function tick(){
  //o render recebe dois parâmetros: o que vai ser carregado e onde será carregado
  ReactDOM.render(
    <React.StrictMode>     
    <App />  {/* recebido da linha 4 */}   
  </React.StrictMode>, 
  document.getElementById('root')
);
//}
//setInterval(tick,1000)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

//TRADUÇÃO 
//Se você deseja começar a medir o desempenho em seu aplicativo, passe uma função para registrar resultados (por exemplo: reportWebVitals(console.log))
// ou envie para um endpoint analítico. Saiba mais: https://bit.ly/CRA-vitals
reportWebVitals();
