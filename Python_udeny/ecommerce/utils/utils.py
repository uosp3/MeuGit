def formata_preco1(val):
    try:
        import locale
        valor_int = float(val)
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        valor_formatado = locale.currency(valor_int, grouping=True)
        return valor_formatado
    except ValueError:
        # Trate o erro
        raise


def formata_preco(valor):
    # Formata o valor com duas casas decimais e separadores de milhar
    valor_formatado = f"{valor:,.2f}"

    # Substitui o separador de milhar e decimal
    # Temporariamente substitui a vírgula para não confundir
    valor_formatado = valor_formatado.replace(",", "X")
    # Troca o ponto pelo separador de milhar (vírgula)
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace(
        "X", ".")  # Coloca o ponto no lugar certo

    return f"R$ {valor_formatado}"


def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])
