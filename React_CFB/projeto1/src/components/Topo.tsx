import Link from "next/link";

export default function Topo(){
    return(
        <div className='flex flex-col justify-between items-center bg-zinc-300 h-[130px]'>
            <div>Logo</div>
                <div className='flex flex-col justify-center items-center'>
                <div className='text-3xl'>CFB Cursos</div>
                <div className='subtituloTopo'>Curso de React</div>
            </div>
            <nav className="flex gap-5">
                <Link href={"/"}>
                    Home
                </Link>
                <Link href={
                        {
                           pathname: "/produtos/Produtos",
                           query:{
                                nome:'Edson',
                                curso:'React Next'
                            }
                        }
                    }>
                    Produtos
                </Link>
                <Link href={"/teste/Teste"}>
                    Teste
                </Link>
                <Link href={"/usestate/Usestate"}>
                    State
                </Link>
                <Link href={"/useeffect/Useeffect"}>
                    Useeffect
                </Link>
                <Link href={"/inputs/Inputs"}>
                    Inputs
                </Link>
                <Link href={"/filtragem/Filtragem"}>
                    Filtragem
                </Link>
            </nav>
        </div>
    )
}