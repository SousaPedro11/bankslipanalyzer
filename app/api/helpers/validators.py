def validate_file_extension(file_name: str, extension: str) -> bool:
    return file_name.upper().endswith(extension)


def regex_digitable_line() -> str:
    """
    Regex to validate the digitable line
    :return: str
    """
    regex_components = [
        "^(?P<campo_1>\\d{5}\\.?\\d{5})",  # Campo 1 - posicoes 1 a 3, 4, 20 a 24 do codigo de barras e dv deste campo
        "\\s?",
        "(?P<campo_2>\\d{5}\\.?\\d{6})",  # Campo 2 - posicoes 25 a 34 do codigo de barras e dv deste campo
        "\\s?",
        "(?P<campo_3>\\d{5}\\.?\\d{6})",  # Campo 3 - posicoes 35 a 44 do codigo de barras e dv deste campo
        "\\s?",
        "(?P<campo_4>\\d)",  # Campo 4 - dv geral do codigo de barras (posicao 5)
        "\\s?",
        "(?P<campo_5>\\d{14})",  # Campo 5 - fator de vencimento (posicao 6 a 9) e valor do documento (posicao 10 a 19)
        "$",
    ]
    return "".join(regex_components)


def regex_barcode() -> str:
    """
    Regex to validate the barcode
    :return: str
    """
    regex_components = [
        "^(?P<banco>\\d{3})",  # Identificação do banco (104)
        "(?P<codigo_moeda>\\d)",  # Código da moeda (9 - Real)
        "(?P<dv_geral>\\d)",  # Dígito verificador geral do código de barras
        "(?P<fator_vencimento>\\d{4})",  # Fator de vencimento
        "(?P<valor_documento>\\d{10})",  # Valor do documento
        "(?P<codigo_beneficiario>\\d{7})",  # Código do beneficiário
        "(?P<sequencia_1>\\d{3})",  # Nosso numero - sequencia 1
        "(?P<constante_1>\\d)",  # Constante 1
        "(?P<sequencia_2>\\d{3})",  # Nosso numero - sequencia 2
        "(?P<constante_2>\\d)",  # Constante 2
        "(?P<sequencia_3>\\d{9})",  # Nosso numero - sequencia 3
        "(?P<dv_campo_livre>\\d)",  # Dígito verificador do campo livre
        "$",
    ]
    return "".join(regex_components)
