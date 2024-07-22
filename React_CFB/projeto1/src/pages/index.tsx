//import Image from 'next/image'
//import { Inter } from 'next/font/google'
//const inter = Inter({ subsets: ['latin'] })

import Topo from "@/components/Topo"
import Card from "@/components/Card"
import Link from "next/link"

const nome="Edson Gomes dos Santos"
let canal="CFBCursos"

export default function Home() {
  return (
    <div>
      <Topo/>{/* tem que ser com letra maiúscula, para usar com minúscula tem que usar {}*/}
      <div style={testecss}>
        <div>Curso de react Next</div>
        <div>Typescript</div>
        <div style={{color:'#f00', backgroundColor:'#bbb'}}>React</div>{/*css em js, inline*/}
      </div>
    </div>
  )
}

const testecss={
  display:'flex',
  justifyContent:'center',
  alignItens:'center',
  color:'#00f',
  backgroundColor: '#eee',
  fontSize:'20px'
}