import SocialNetworks from "./SocialNetworks"

import Avatar from "../img/Face.jpg"

import "../styles/components/sidebar.sass"
import InformationContainer from "./InformationContainer"

const Sidebar = () => {
  return (
    <aside id="sidebar">
      <img src={Avatar} alt="Edson Gomes"></img>
      <p className="title">Desenvolvedor</p>
      <SocialNetworks/>
      <InformationContainer/>
      <a href="" className="btn">
        Download currículo
      </a>
    </aside>
  )
}

export default Sidebar
