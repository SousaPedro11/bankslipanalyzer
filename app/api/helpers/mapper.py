CODE_ERRORS = {
    401: "unauthorized",
    403: "forbidden",
    404: "not-found",
    405: "method-not-allowed",
    422: "validation-error",
    500: "internal-error",
}


NEXXERA_RETURN_MOVEMENT_CODE = {
    "02": "Entrada Confirmada",
    "03": "Entrada Rejeitada",
    "04": "Transferência de Carteira/Entrada",
    "05": "Transferência de Carteira/Baixa",
    "06": "Liquidação",
    "07": "Confirmação do Recebimento da Instrução de Desconto",
    "08": "Confirmação do Recebimento do Cancelamento do Desconto",
    "09": "Baixa",
    "11": "Títulos em Carteira (Em Ser)",
    "12": "Confirmação Recebimento Instrução de Abatimento",
    "13": "Confirmação Recebimento Instrução de Cancelamento Abatimento",
    "14": "Confirmação Recebimento Instrução Alteração de Vencimento",
    "15": "Franco de Pagamento",
    "16": "Abatimento Alterado",
    "17": "Liquidação Após Baixa ou Liquidação Título Não Registrado",
    "18": "Acerto de Depositária (sem motivo)",
    "19": "Confirmação Recebimento Instrução de Protesto",
    "20": "Confirmação Recebimento Instrução de Sustação/Cancelamento de Protesto",
    "21": "Acerto do controle do participante",
    "22": "Título Com Pagamento Cancelado",
    "23": "Remessa a Cartório (Aponte em Cartório)",
    "24": "Retirada de Cartório e Manutenção em Carteira",
    "25": "Protestado e Baixado (Baixa por Ter Sido Protestado)",
    "26": "Instrução Rejeitada",
    "27": "Confirmação do Pedido de Alteração de Outros Dados",
    "28": "Débito de Tarifas/Custas",
    "29": "Ocorrências do Sacado",
    "30": "Alteração de Dados Rejeitada",
    "31": "Cancelamento Abatimento Rejeitado",
    "32": "Estorno de protesto",
    "33": "Confirmação da Alteração dos Dados do Rateio de Crédito",
    "34": "Confirmação do Cancelamento dos Dados do Rateio de Crédito",
    "35": "Confirmação do Desagendamento do Débito Automático",
    "36": "Baixa Rejeitada",
    "37": "Cobrança Contratual – Abatimento e Baixa Bloqueados",
    "38": "Confirmação Recebimento de Instrução de Não Protestar",
    "39": "Alteração do Nome do Sacado",
    "40": "Alteração do Endereço do Sacado",
    "41": "Alteração do Tipo de Cobrança",
    "42": "Débito em conta",
    "43": "Dispensar Juros",
    "44": "Manutenção de título vencido",
    "45": "Conceder desconto",
    "46": "Não conceder desconto",
    "47": "Retificar desconto",
    "48": "Alterar data para desconto",
    "49": "Cobrança de multa",
    "50": "Dispensa de multa",
    "51": "Dispensa de indexador",
    "52": "Dispensa do prazo limite para recebimento do título",
    "53": "Alteração do prazo limite para recebimento do título",
    "54": "Alteração de tipo de cobrança especifico para títulos das carteiras 1 e D",
    "55": "Solicitação encaminhada à Agencia",
    "56": "Crédito no C/C Conta Garantida",
    "57": "Título já Baixado/Liquidado",
    "58": "Título não existe",
    "59": "Cobrança a Creditar",
    "60": "Situação do Título – Cartório",
    "61": "Baixa com crédito direto com valor do crédito informado",
    "62": "Confirmação da alteração do campo seu número",
    "63": "Emissão de Carta de Protesto",
    "64": "Protesto não sustado",
    "65": "Protesto devolvido pelo cartório",
    "66": "Multa alterada",
    "67": "Multa cancelada",
    "68": "Amortização",
    "69": "Baixado e Creditado em Conta Corrente – Adiant Fornecedores",
    "70": "Alteração De Dados - Nova Entrada",
    "71": "Alteração De Dados – Baixa",
    "72": "Baixa Com Transferência Para Desconto",
    "73": "Prazo de Devolução Alterado",
    "74": "Alteração Confirmada",
    "75": "Alteração com Remissão de Bloqueto confirmada",
    "76": "Alteração da Opção de Protesto para devolução Confirmada",
    "77": "Alteração da opção de Devolução para protesto confirmada",
    "78": "Protesto Rejeitado",
    "79": "Abatimento Rejeitado",
    "80": "Instrução Cancelada",
    "81": "Estorno de Sustação de Protesto",
    "82": "Prorrogação vencimento rejeitada",
    "83": "Cancelar protesto rejeitado – Fora de Prazo",
    "84": "Código ocorrência inválido",
    "85": "Estorno de Baixa/Liquidação",
    "86": "Alteração de seu número rejeitada",
    "87": "Não protestar rejeitado",
    "88": "Liquidação parcial efetuada",
    "89": "Liquidação parcial rejeitada",
    "90": "Dispensar juros de mora rejeitado",
    "91": "Uso do banco",
    "92": "Título liquidado no banco correspondente",
    "93": "Título liquidado no cartório do banco correspondente",
    "94": "Baixado creditado diretamente",
    "95": "Uso da Empresa Alterado",
    "96": "Prazo de Protesto Alterado",
    "97": "Alteração de juros de mora",
    "98": "Liquidação Cobrança Garantida S/ Crédito no C/C",
    "99": "Outros",
    "AA": "Transferência Cobrança Garantida para CS",
    "AB": "Título descontado transferido para cobrança simples c/ débito em conta",
    "AC": "Título descontado liquidado com débito em conta",
    "AD": "Alterações específicas da Agencia Bancária – Não Considerar",
    "AE": "Título Sustado Judicialmente",
    "AF": "Transferência de Cedente",
    "AG": "Sustação não acatada",
    "AH": "Juros e Data de Vencimento alterado",
    "AI": "Transferência de Carteira/Desconto",
    "AJ": "Número de Autorização Inexistente",
    "AK": "Título Não Processado",
    "AL": "Alteração de Instrução",
    "AM": "Aguardando Autorização para Protesto por edital",
    "AN": "Protesto Sustado por Alteração de Vencimento e Prazo de Cartório",
    "AO": "Título em Trânsito Pago em Cartório",
    "AP": "Reembolso e Transferência",
    "AQ": "Reembolso e Devolução",
    "AR": "Alteração de Títulos",
    "AS": "Relação de Títulos",
    "AT": "Manutenção Mensal",
    "AU": "Sustação de Cartório e Envio de Título à Cartório",
    "AV": "Fornecimento de formulário pré-impresso",
    "AW": "Estorno Liquidação Parcial",
    "AX": "Devolvido Conforme Instrução",
    "AY": "Devolvido",
    "AZ": "Estorno Devolvido",
    "BA": "Confirmação Invalida",
    "BB": "Pendente para Próxima Fita",
    "BC": "Inconsistência Pendente",
    "BD": "Confirmação de envio de e-mail/SMS",
    "BE": "Envio de e-mail/SMS rejeitado",
    "BF": "Liquidado com Cheque a Compensar",
    "BG": "Instrução Codificada",
    "BH": "Emissão de Segunda Via de Aviso",
    "BI": "Não Conceder Juros Fora do Prazo",
    "BJ": "Protesto Devolvido para Cartório",
    "BK": "Pagamento",
    "BL": "Cobrança Parcial",
    "BM": "Instrução Confirmada",
    "BN": "Entrada Confirmada Com Rateio de Crédito",
    "BO": "Cheque Devolvido",
    "BP": "Baixa por Crédito em C/C sem Título Correspondente",
    "BQ": "Confirmação de Entrada na Cobrança Simples – Entrada Não Aceita na Cobrança Contratual",
    "BR": "Título Para Cobrança em Bancos Correspondentes",
    "BS": "Remessa Já Enviada",
    "BT": "Título Reativado",
    "BU": "Liquidação de Título Vencido",
    "BV": "Título Reclassificado - Título sofreu liquidação reclassificada",
    "BW": "Título Pendente de Qualificação – (Carteira Caução)",
    "BX": "Solicitação de Impressão de Títulos Confirmada",
    "BY": "Confirmação de Inclusão Banco de Sacado",
    "BZ": "Confirmação de Alteração Banco de Sacado",
    "CA": "Confirmação de Exclusão Banco de Sacado",
    "CB": "Emissão de Bloquetos de Banco de Sacado",
    "CC": "Manutenção de Sacado Rejeitada",
    "CD": "Entrada de Título via Banco de Sacado Rejeitada",
    "CE": "Manutenção de banco de Sacado Rejeitada",
    "CF": "Confirmação da Alteração dos Dados do Sacado",
    "CG": "Confirmação da Alteração dos Dados do Sacador/Avalista",
    "CH": "Título Pago com Cheque Devolvido",
    "CI": "Título Pago com Cheque Compensado",
    "CJ": "Instrução para Cancelar Protesto Confirmada",
    "CK": "Instrução para Protesto para Fins falimentares Confirmada",
    "CL": "Confirmação de Instrução de transferência de Carteira/Modalidade de Cobrança",
    "CM": "Alteração de Contrato de Cobrança",
    "CN": "Título DDA Reconhecido Pelo Sacado",
    "CO": "Título DDA Não Reconhecido Pelo Sacado",
    "CP": "Título DDA Recusado Pela CIP",
    "CQ": "Confirmação da Instrução de Baixa de Título Negativado Sem Protesto",
    "CR": "Entrada Registrada Aguardando Avaliação",
    "CS": "Cancelamento do Título",
    "CT": "Confirmação de Pedido de Exclusao de Negativação",
    "CU": "Título enviado para Negativação",
    "CV": "Movimentação na CIP",
    "CW": "Negativação Expressa Informacional",
    "CX": "Confirmação de Entrada em Negativação Expressa/Tarifa",
    "CY": "Confirmação de Cancelamento em Negativação expressa/Tarifa",
    "CZ": "Confirmação Exclusão de Entrada em Negativação Expressa por Liquidação/Tarifa",
    "DA": "Confirmação Recebimento de Instrução de Não Negativar",
    "DB": "Confirmação de Alteração do Valor Nominal do Título",
    "DC": "Título Sustado Judicialmente",
}
