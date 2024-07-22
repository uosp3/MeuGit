import Card from "@/components/Card"
import Topo from "@/components/Topo"
import { useRouter } from "next/router"

const produtos=[
    {
        id:1,
        produto: 'Mouse',
        valor: 49.9,
        desconto:0,
        disponivel:true
    },
    {
        id:2,
        produto: 'Teclado',
        valor: 69.9,
        desconto:10,
        disponivel:true
    },
    {
        id:3,
        produto: 'Monitor',
        valor: 659.9,
        desconto:0,
        disponivel:true
    },
    {
        id:4,
        produto: 'CPU',
        valor: 829.9,
        desconto:100,
        disponivel:true
    },
    {
        id:5,
        produto: 'Cx.Som',
        valor: 39.9,
        desconto:0,
        disponivel:true
    },
    {
        id:6,
        produto: 'Microfone',
        valor: 65.0,
        desconto:0,
        disponivel:true
    }
]

function calcDesc(v:number, d:number){
    return v-d
  }
  
  function calcDesc2(v:number, d:number){
    return v-(d/2)
  }

export default function ProdutosPagina(){ // eslint-disable-next-line react-hooks/rules-of-hooks
    const router=useRouter()
    //const nome=router.query.nome
    //const curso=router.query.curso
    const {nome,curso}=router.query //esta linha faz o mesmo que as duas acima.
    console.log(nome)
    console.log(curso)
    return(
        <div>
            <Topo/>
            <div className="flex justify-center gap-3">
                {
                produtos.map((e:any)=>{
                    if(e.disponivel){
                        return(
                        <Card key={e.id} produto={e.produto} valor={e.valor} desconto={e.desconto} funcao={calcDesc}>
                            <div>Curso de React Next</div>
                            <div>CFBCursos</div>
                        </Card>              
                        )}
                    })
                } 
            </div> 
        </div>
    )
}