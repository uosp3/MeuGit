const List = () => {
  const itens = [
    { id: 1, name: "Matheus" },
    { id: 2, name: "Edson" },
    { id: 3, name: "Pedro" },
  ]
  return (
    <div>
      {itens.map((item) => (
        <p key={item.id}>
          {item.id} - {item.name}
        </p>
      ))}
    </div>
  )
}

export default List
