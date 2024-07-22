const burrinho = () => {
  return (
    <div>
        Fluxo de renderização

        1 - Toda vez que alteramos o estado de um componente, TODO componente é recalculado
        2 - Toda vez que o seu compenente PAI renderizar
        3 - Toda vez que alguma das suas propriedades mudarem

        Algoritmo de reconciliação

        1 - Criar em memória a nova versão do HTML do componente.
        2 - Compara essa nova versão com a versão anterior ao HTML (Diff)
        3 - Aplicar as operações javaescript para alterar somente o necessário do HTML
    </div>
  )
}
