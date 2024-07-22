import MainContent from './components/MainContent'
import Sidebar from './components/Sidebar'

import './styles/components/App.sass'

function App() {
  return (
    <div id="portfolio">
      <h1>Edson Gomes</h1>
      <Sidebar/>
      <MainContent/>
    </div>
  )
}

export default App
