import re
from typing import List

from starlette.exceptions import HTTPException


def validate_file_extension(file_name: str, extension: str):
    if not file_name.upper().endswith(extension):
        raise HTTPException(status_code=400, detail=f"Invalid file extension. Expected {extension}")


def validate_lpn_file(file_name: str):
    regex = "LPN\\d{1,16}.REM"

    if not (re.match(regex, file_name) or validate_file_extension(file_name, ".REM")):
        raise HTTPException(status_code=400, detail="Invalid file name. Expected LPN*.REM")


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
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>0{4})",  # Lote de servico
        "(?P<registro>0)",  # Tipo de registro
        "(?P<filler>\\s{9})",  # Uso Exclusivo NEXXERA
        "(?P<inscricao_tipo>\\d)",  # Tipo de inscricao da empresa
        "(?P<inscricao_numero>\\d{14})",  # Numero de inscricao da empresa
        "(?P<convenio>.{20})",  # Codigo do convenio no banco
        "(?P<agencia_codigo>\\d{5})",  # Agencia mantenedora da conta
        "(?P<agencia_dv>.{1})",  # Digito verificador da agencia
        "(?P<conta_numero>\\d{12})",  # Numero da conta corrente
        "(?P<conta_dv>.{1})",  # Digito verificador da conta
        "(?P<ag_conta_dv>.{1})",  # Digito verificador da agencia/conta
        "(?P<empresa_nome>.{30})",  # Nome da empresa
        "(?P<banco_nome>.{30})",  # Nome do banco
        "(?P<van_nome>.{10})",  # Nome da VAN
        "(?P<arquivo_codigo>\\d)",  # Codigo remessa/retorno
        "(?P<arquivo_geracao_data>\\d{8})",  # Data de geracao do arquivo
        "(?P<arquivo_geracao_hora>\\d{6})",  # Hora de geracao do arquivo
        "(?P<arquivo_sequencia>\\d{7})",  # Numero sequencial do arquivo
        "(?P<arquivo_layout>020)",  # Numero da versao do layout do arquivo
        "(?P<arquivo_densidade>\\d{5})",  # Densidade de gravacao do arquivo
        "(?P<reservado_banco>.{19})",  # Uso exclusivo do banco
        "(?P<reservado_empresa>.{20})",  # Uso exclusivo da empresa
        "(?P<observacoes>.{29})",  # Observacao do layout bancario
        "$",
    ]

    return "".join(regex_components)


def regex_lot_header_nexxera():
    """
    Regex to validate the lot header from Nexxera
    :return: str
    """

    regex_components = [
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>\\d{4})",  # Lote de servico
        "(?P<registro>1)",  # Tipo de registro
        "(?P<operacao>.{1})",  # Tipo de operacao
        "(?P<servico>\\d{2})",  # Tipo de servico
        "(?P<filler>\\s{2})",  # Uso Exclusivo NEXXERA
        "(?P<versao_layout>\\d{3})",  # Versao do layout do lote
        "(?P<filler_2>\\s{1})",  # Uso Exclusivo NEXXERA
        "(?P<inscricao_tipo>\\d)",  # Tipo de inscricao da empresa
        "(?P<inscricao_numero>\\d{15})",  # Numero de inscricao da empresa
        "(?P<convenio>.{20})",  # Codigo do convenio no banco
        "(?P<agencia_codigo>\\d{5})",  # Agencia mantenedora da conta
        "(?P<agencia_dv>.{1})",  # Digito verificador da agencia
        "(?P<conta_numero>\\d{12})",  # Numero da conta corrente
        "(?P<conta_dv>.{1})",  # Digito verificador da conta
        "(?P<ag_conta_dv>.{1})",  # Digito verificador da agencia/conta
        "(?P<empresa_nome>.{30})",  # Nome da empresa
        "(?P<mensagem>.{40})",  # Mensagem 1
        "(?P<mensagem_2>.{40})",  # Mensagem 2
        "(?P<numero_remessa>\\d{8})",  # Numero da remessa/retorno
        "(?P<data_gravacao>\\d{8})",  # Data de gravacao da remessa/retorno
        "(?P<data_credito>\\d{8})",  # Data do credito
        "(?P<modelo_cod>.{7})",  # Codigo de modelo personalizado
        "(?P<filler_3>\\s{26})",  # Uso Exclusivo NEXXERA
        "$",
    ]

    return "".join(regex_components)


def regex_p_segment_nexxera():
    """
    Regex to validate the P segment from Nexxera
    :return: str
    """

    regex_components = [
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>\\d{4})",  # Lote de servico
        "(?P<registro>3)",  # Tipo de registro
        "(?P<numero_registro>\\d{5})",  # Numero sequencial do registro no lote
        "(?P<segmento>P)",  # Codigo do segmento do registro detalhe
        "(?P<filler>\\s{1})",  # Uso Exclusivo NEXXERA
        "(?P<movimento_codigo>.{2})",  # Codigo de movimento remessa
        "(?P<agencia_codigo>\\d{5})",  # Agencia mantenedora da conta
        "(?P<agencia_dv>.{1})",  # Digito verificador da agencia
        "(?P<conta_numero>\\d{12})",  # Numero da conta corrente
        "(?P<conta_dv>.{1})",  # Digito verificador da conta
        "(?P<ag_conta_dv>.{1})",  # Digito verificador da agencia/conta
        "(?P<nosso_numero>.{20})",  # Nosso numero
        "(?P<carteira_codigo>.{1})",  # Codigo da carteira
        "(?P<cadastramento>\\d)",  # Tipo de cadastramento
        "(?P<documento>.{1})",  # Tipo de documento de cobranca
        "(?P<emissao_bloqueto>.{1})",  # Emissao do bloqueto
        "(?P<distribuicao_bloqueto>.{1})",  # Distribuicao do bloqueto
        "(?P<documento_numero>.{15})",  # Numero do documento de cobranca
        "(?P<vencimento>\\d{8})",  # Data de vencimento do titulo
        "(?P<valor>\\d{15})",  # Valor nominal do titulo
        "(?P<agencia_cobranca_codigo>\\d{5})",  # Agencia cobradora
        "(?P<agencia_cobranca_dv>.{1})",  # Digito verificador da agencia cobradora
        "(?P<especie_codigo>\\d{2})",  # Especie do titulo
        "(?P<aceite>.{1})",  # Identificacao do titulo aceito/não aceito
        "(?P<emissao>\\d{8})",  # Data de emissao do titulo
        "(?P<juros_mora_codigo>\\d{1})",  # Codigo do juros de mora
        "(?P<juros_mora_data>\\d{8})",  # Data do juros de mora
        "(?P<juros_mora_taxa>\\d{15})",  # Juros de mora por dia/taxa
        "(?P<desconto_codigo>\\d{1})",  # Codigo do desconto 1
        "(?P<desconto_data>\\d{8})",  # Data do desconto 1
        "(?P<desconto_valor>\\d{15})",  # Valor/percentual a ser concedido
        "(?P<valor_iof>\\d{15})",  # Valor do IOF a ser recolhido
        "(?P<valor_abatimento>\\d{15})",  # Valor do abatimento
        "(?P<identificacao_titulo_empresa>.{25})",  # Identificacao do titulo na empresa
        "(?P<codigo_protesto>\\d{1})",  # Codigo para protesto
        "(?P<prazo_protesto>\\d{2})",  # Prazo para protesto
        "(?P<codigo_baixa>\\d{1})",  # Codigo para baixa/devolucao
        "(?P<prazo_baixa>.{3})",  # Prazo para baixa/devolucao
        "(?P<moeda_codigo>\\d{2})",  # Codigo da moeda
        "(?P<contrato_numero>\\d{10})",  # Numero do contrato da operacao de credito
        "(?P<uso_livre>.{1})",  # Uso livre
        "$",
    ]

    return "".join(regex_components)


def regex_q_segment_nexxera():
    """
    Regex to validate the Q segment from Nexxera
    :return:
    """
    regex_components = [
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>\\d{4})",  # Lote de servico
        "(?P<registro>3)",  # Tipo de registro
        "(?P<numero_registro>\\d{5})",  # Numero sequencial do registro no lote
        "(?P<segmento>Q)",  # Codigo do segmento do registro detalhe
        "(?P<filler>\\s{1})",  # Uso Exclusivo NEXXERA
        "(?P<movimento_codigo>.{2})",  # Codigo de movimento remessa
        "(?P<sacado_inscricao_tipo>\\d{1})",  # Tipo de inscricao
        "(?P<sacado_inscricao_numero>\\d{15})",  # Numero de inscricao
        "(?P<sacado_nome>.{40})",  # Nome
        "(?P<sacado_endereco>.{40})",  # Endereco
        "(?P<sacado_bairro>.{15})",  # Bairro
        "(?P<sacado_cep>\\d{5})",  # CEP
        "(?P<sacado_cep_sufixo>\\d{3})",  # Sufixo do CEP
        "(?P<sacado_cidade>.{15})",  # Cidade
        "(?P<sacado_uf>.{2})",  # UF
        "(?P<avalista_inscricao_tipo>\\d{1})",  # Tipo de inscricao do avalista
        "(?P<avalista_inscricao_numero>\\d{15})",  # Numero de inscricao do avalista
        "(?P<avalista_nome>.{40})",  # Nome do avalista
        "(?P<banco_correspondente_codigo>\\d{3})",  # Codigo do banco correspondente na compensacao
        "(?P<banco_correspondente_nosso_numero>.{20})",  # Nosso numero no banco correspondente
        "(?P<acesso_boleto>.{1})",  # Acesso ao boleto
        "(?P<instrucao_cobranca_primeira>.{2})",  # Instrucao de cobranca 1
        "(?P<instrucao_cobranca_segunda>.{2})",  # Instrucao de cobranca 2
        "(?P<variacao_carteira>\\d{3})",  # Variacao da carteira
        "$",
    ]

    return "".join(regex_components)


def regex_r_segment_nexxera():
    """
    Regex to validate the R segment from Nexxera
    :return:
    """
    regex_components = [
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>\\d{4})",  # Lote de servico
        "(?P<registro>3)",  # Tipo de registro
        "(?P<numero_registro>\\d{5})",  # Numero sequencial do registro no lote
        "(?P<segmento>R)",  # Codigo do segmento do registro detalhe
        "(?P<filler>\\s{1})",  # Uso Exclusivo NEXXERA
        "(?P<movimento_codigo>.{2})",  # Codigo de movimento remessa
        "(?P<desconto_2_codigo>.{1})",  # Codigo do desconto 2
        "(?P<desconto_2_data>\\d{8})",  # Data do desconto 2
        "(?P<desconto_2_valor>\\d{15})",  # Valor/percentual a ser concedido
        "(?P<desconto_3_codigo>.{1})",  # Codigo do desconto 3
        "(?P<desconto_3_data>\\d{8})",  # Data do desconto 3
        "(?P<desconto_3_valor>\\d{15})",  # Valor/percentual a ser concedido
        "(?P<multa_codigo>.{1})",  # Codigo da multa
        "(?P<multa_data>\\d{8})",  # Data da multa
        "(?P<multa_valor>\\d{15})",  # Valor da multa
        "(?P<informacao_sacado>.{10})",  # Informacao ao sacado
        "(?P<informacao_3>.{40})",  # Mensagem 3
        "(?P<informacao_4>.{40})",  # Mensagem 4
        "(?P<filler_2>\\s{8})",  # Uso Exclusivo NEXXERA
        "(?P<carne_numero>.{6})",  # Numero do carne
        "(?P<carne_parcela>\\d{3})",  # Parcela do carne
        "(?P<carne_total_parcelas>\\d{3})",  # Total de parcelas do carne
        "(?P<ocorrencia_sacado_codigo>\\d{8})",  # Codigo da ocorrencia do sacado
        "(?P<debito_banco_codigo>\\d{3})",  # Codigo do banco para debito
        "(?P<debito_agencia_codigo>\\d{5})",  # Agencia para debito
        "(?P<debito_agencia_dv>\\d{1})",  # DV da agencia para debito
        "(?P<debito_conta_numero>\\d{12})",  # Conta para debito
        "(?P<debito_conta_dv>.{1})",  # DV da conta para debito
        "(?P<debito_agencia_conta_dv>.{1})",  # DV da agencia/conta para debito
        "(?P<debito_automatico_aviso>\\d{1})",  # Aviso ao debito automatico
        "(?P<filler_3>\\s{9})",  # Uso Exclusivo NEXXERA
        "$",
    ]

    return "".join(regex_components)


def regex_s_segment_nexxera():
    return ""


def regex_t_segment_nexxera():
    """
    Regex to validate the T segment from Nexxera
    :return:
    """
    regex_components = [
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>\\d{4})",  # Lote de servico
        "(?P<registro>3)",  # Tipo de registro
        "(?P<numero_registro>\\d{5})",  # Numero sequencial do registro no lote
        "(?P<segmento>T)",  # Codigo do segmento do registro detalhe
        "(?P<filler>\\s{1})",  # Uso Exclusivo NEXXERA
        "(?P<movimento_codigo>.{2})",  # Codigo de movimento remessa
        "(?P<agencia_codigo>\\d{5})",  # Agencia mantenedora da conta
        "(?P<agencia_dv>.{1})",  # DV da agencia mantenedora da conta
        "(?P<conta_numero>\\d{12})",  # Numero da conta corrente
        "(?P<conta_dv>.{1})",  # DV da conta corrente
        "(?P<agencia_conta_dv>.{1})",  # DV da agencia/conta
        "(?P<nosso_numero>.{20})",  # Identificacao do titulo no banco
        "(?P<carteira_codigo>.{1})",  # Codigo da carteira
        "(?P<documento_numero>.{15})",  # Numero do documento de cobranca
        "(?P<vencimento_data>\\d{8})",  # Data de vencimento do titulo
        "(?P<valor>\\d{15})",  # Valor nominal do titulo
        "(?P<banco_recebedor_codigo>\\d{3})",  # Codigo do banco recebedor
        "(?P<agencia_recebedora_codigo>\\d{5})",  # Agencia recebedora
        "(?P<agencia_recebedora_dv>.{1})",  # DV da agencia recebedora
        "(?P<exclusivo_empresa>.{25})",  # Uso Exclusivo da Empresa
        "(?P<moeda_codigo>\\d{2})",  # Codigo da moeda
        "(?P<sacado_tipo_inscricao>\\d{1})",  # Tipo de inscricao do sacado
        "(?P<sacado_numero_inscricao>\\d{15})",  # Numero de inscricao do sacado
        "(?P<sacado_nome>.{40})",  # Nome do sacado
        "(?P<contrato_numero>\\d{10})",  # Numero do contrato
        "(?P<tarifa_valor>\\d{15})",  # Valor da tarifa
        "(?P<ocorrencia_motivo>.{10})",  # Motivo da ocorrencia
        "(?P<filler_1>.{14})",  # Uso Exclusivo NEXXERA
        "(?P<variacao_carteira_codigo>\\d{3})",  # Codigo da variacao da carteira
        "$",
    ]

    return "".join(regex_components)


def regex_u_segment_nexxera():
    return ""


def regex_v_segment_nexxera():
    return ""


def regex_w_segment_nexxera():
    return ""


def regex_y_segment_nexxera():
    return ""


def verify_segment_pattern(line: str, segments_pattern: List[str]):
    return any(re.match(pattern, line) for pattern in segments_pattern)


def is_shipping_segment_nexxera(line: str) -> bool:
    segments_pattern = [
        regex_p_segment_nexxera(),
        regex_q_segment_nexxera(),
        regex_r_segment_nexxera(),
    ]

    return verify_segment_pattern(line, segments_pattern)


def is_return_segment_nexxera(line: str) -> bool:
    segments_pattern = [
        regex_t_segment_nexxera(),
    ]

    return verify_segment_pattern(line, segments_pattern)


def regex_lot_trailer_nexxera() -> str:
    """
    Regex to validate the lot trailer from Nexxera
    :return: str
    """

    regex_components = [
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>\\d{4})",  # Lote de servico
        "(?P<registro>5)",  # Tipo de registro
        "(?P<filler>\\s{9})",  # Uso Exclusivo FEBRABAN/CNAB
        "(?P<qtd_registros_lote>\\d{6})",  # Quantidade de registros do lote
        "(?P<cobranca_simples_qtd>\\d{6})",  # Quantidade de titulos em cobranca simples
        "(?P<cobranca_simples_valor>\\d{17})",  # Valor total dos titulos em cobranca simples
        "(?P<cobranca_vinculada_qtd>\\d{6})",  # Quantidade de titulos em cobranca vinculada
        "(?P<cobranca_vinculada_valor>\\d{17})",  # Valor total dos titulos em cobranca vinculada
        "(?P<cobranca_caucionada_qtd>\\d{6})",  # Quantidade de titulos em cobranca caucionada
        "(?P<cobranca_caucionada_valor>\\d{17})",  # Valor total dos titulos em cobranca caucionada
        "(?P<cobranca_descontada_qtd>\\d{6})",  # Quantidade de titulos em cobranca descontada
        "(?P<cobranca_descontada_valor>\\d{17})",  # Valor total dos titulos em cobranca descontada
        "(?P<aviso_numero>.{8})",  # Numero do aviso de lancamento
        "(?P<filler_2>\\s{117})",  # Uso Exclusivo NEXXERA
        "$",
    ]

    return "".join(regex_components)


def regex_file_trailer_nexxera() -> str:
    """
    Regex to validate the file trailer from Nexxera
    :return: str
    """

    regex_components = [
        "^(?P<banco>\\d{3})",  # Cod. do Banco na Compensacao
        "(?P<lote>9999)",  # Lote de servico
        "(?P<registro>9)",  # Tipo de registro
        "(?P<filler>\\s{9})",  # Uso Exclusivo NEXXERA
        "(?P<qtd_lotes>\\d{6})",  # Quantidade de lotes do arquivo
        "(?P<qtd_registros>\\d{6})",  # Quantidade de registros do arquivo
        "(?P<qtd_contas>\\d{6})",  # Quantidade de contas do arquivo
        "(?P<filler_2>\\s{205})",  # Uso Exclusivo NEXXERA
        "$",
    ]

    return "".join(regex_components)
