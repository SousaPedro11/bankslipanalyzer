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


def regex_file_header_nexxera() -> str:
    """
    Regex to validate the file header from Nexxera
    :return: str
    """

    regex_components = [
        "^(?<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?<lote>0{4})",  # Lote de servico
        "(?<registro>0)",  # Tipo de registro
        "(?<filler>\\s{9})",  # Uso Exclusivo NEXXERA
        "(?<inscricao_tipo>\\d)",  # Tipo de inscricao da empresa
        "(?<inscricao_numero>\\d{14})",  # Numero de inscricao da empresa
        "(?<convenio>.{20})",  # Codigo do convenio no banco
        "(?<agencia_codigo>\\d{5})",  # Agencia mantenedora da conta
        "(?<agencia_dv>.{1})",  # Digito verificador da agencia
        "(?<conta_numero>\\d{12})",  # Numero da conta corrente
        "(?<conta_dv>.{1})",  # Digito verificador da conta
        "(?<ag_conta_dv>.{1})",  # Digito verificador da agencia/conta
        "(?<empresa_nome>.{30})",  # Nome da empresa
        "(?<banco_nome>.{30})",  # Nome do banco
        "(?<van_nome>.{10})",  # Nome da VAN
        "(?<arquivo_codigo>\\d)",  # Codigo remessa/retorno
        "(?<arquivo_geracao_data>\\d{8})",  # Data de geracao do arquivo
        "(?<arquivo_geracao_hora>\\d{6})",  # Hora de geracao do arquivo
        "(?<arquivo_sequencia>\\d{7})",  # Numero sequencial do arquivo
        "(?<arquivo_layout>020)",  # Numero da versao do layout do arquivo
        "(?<arquivo_densidade>\\d{5})",  # Densidade de gravacao do arquivo
        "(?<reservado_banco>.{19})",  # Uso exclusivo do banco
        "(?<reservado_empresa>.{20})",  # Uso exclusivo da empresa
        "(?<observacoes>.{29})",  # Observacao do layout bancario
    ]

    return "".join(regex_components)


def regex_file_trailer_nexxera() -> str:
    """
    Regex to validate the file trailer from Nexxera
    :return: str
    """

    regex_components = [
        "^(?<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?<lote>9999)",  # Lote de servico
        "(?<registro>9)",  # Tipo de registro
        "(?<filler>\\s{9})",  # Uso Exclusivo NEXXERA
        "(?<qtd_lotes>\\d{6})",  # Quantidade de lotes do arquivo
        "(?<qtd_registros>\\d{6})",  # Quantidade de registros do arquivo
        "(?<qtd_contas>\\d{6})",  # Quantidade de contas do arquivo
        "(?<filler2>\\s{205})",  # Uso Exclusivo NEXXERA
    ]

    return "".join(regex_components)
