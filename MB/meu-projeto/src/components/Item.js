import PropTypes from 'prop-types'

function Item({marca, ano_lancamento}){
    return(
        <>
            <li>{marca} - {ano_lancamento}</li>            
        </>
    )

}

Item.propTypes = {
    marca: PropTypes.string.isRequired,//força que o valor seja requerido e tem que ser uma string (o erro aparece no console)
    ano_lancamento: PropTypes.number,//força que o valor seja número
}

Item.defaultProps = {//força a entrada dos dados, caso contrário da o aviso abaixo.
    marca: 'Faltou a marca',
    ano_lancamento: 0,
}

export default Item