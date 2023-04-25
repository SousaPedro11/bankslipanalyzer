from typing import List, Optional, Text, Union

from pydantic import BaseModel, Field


class BankSlipShippingSchema(BaseModel):
    content: str


class ShippingInputSchema(BaseModel):
    content: Text


class FileLineSchema(BaseModel):
    file_line: int


class FileHeaderSchema(FileLineSchema):
    bank: str = Field(..., description="Bank identifier", example="104", min_length=3, max_length=3)
    lot: str = Field(..., description="Lot identifier", example="0001", min_length=4, max_length=4)
    registry_type: str = Field(..., description="Registry type", example="0", min_length=1, max_length=1)
    filler: str = Field(..., description="Filler", example=" " * 9, min_length=9, max_length=9)
    inscription_type: str = Field(
        ...,
        description="Enterprise inscription type",
        example="1",
        min_length=1,
        max_length=1,
    )
    inscription_number: str = Field(
        ...,
        description="Enterprise inscription number",
        example="00000000000000",
        min_length=14,
        max_length=14,
    )
    covenant: str = Field(..., description="Covenant", example="0" * 20, min_length=20, max_length=20)
    agency_code: str = Field(..., description="Agency code", example="00000", min_length=5, max_length=5)
    agency_vd: str = Field(..., description="Agency verification digit", example="0", min_length=1, max_length=1)
    account_number: str = Field(..., description="Account number", example="0" * 12, min_length=12, max_length=12)
    account_vd: str = Field(..., description="Account verification digit", example="0", min_length=1, max_length=1)
    agency_account_vd: str = Field(
        ...,
        description="Agency/Account verification digit",
        example="0",
        min_length=1,
        max_length=1,
    )
    enterprise_name: str = Field(..., description="Enterprise name", example="a" * 30, min_length=30, max_length=30)
    bank_name: str = Field(..., description="Bank name", example="a" * 30, min_length=30, max_length=30)
    van_name: str = Field(..., description="Van name", example="NEXXERA   ", min_length=10, max_length=10)
    file_code: str = Field(..., description="File code", example="1", min_length=1, max_length=1)
    file_generation_date: str = Field(
        ...,
        description="File generation date",
        example="00000000",
        min_length=8,
        max_length=8,
    )
    file_generation_hour: str = Field(
        ...,
        description="File generation hour",
        example="000000",
        min_length=6,
        max_length=6,
    )
    file_sequential_number: str = Field(
        ...,
        description="File sequential number",
        example="0" * 7,
        min_length=7,
        max_length=7,
    )
    file_layout_version: str = Field(..., description="File layout version", example="020", min_length=3, max_length=3)
    file_density: str = Field(..., description="File density", example="00000", min_length=5, max_length=5)
    bank_reserved: str = Field(..., description="Bank reserved", example="a" * 19, min_length=19, max_length=19)
    enterprise_reserved: str = Field(
        ...,
        description="Enterprise reserved",
        example="a" * 20,
        min_length=20,
        max_length=20,
    )
    bank_observations: str = Field(..., description="Bank observations", example="a" * 29, min_length=29, max_length=29)


class FileTrailerSchema(FileLineSchema):
    bank: str = Field(..., description="Bank identifier", example="104", min_length=3, max_length=3)
    lot: str = Field(..., description="Lot identifier", example="9999", min_length=4, max_length=4)
    registry_type: str = Field(..., description="Registry type", example="9", min_length=1, max_length=1)
    filler: str = Field(..., description="Filler", example=" " * 9, min_length=9, max_length=9)
    total_lots: str = Field(..., description="Total lots", example="000001", min_length=6, max_length=6)
    total_registries: str = Field(..., description="Total registries", example="000000", min_length=6, max_length=6)
    total_accounts: str = Field(..., description="Total accounts", example="000000", min_length=6, max_length=6)
    filler_2: str = Field(..., description="Filler", example=" " * 205, min_length=205, max_length=205)


class LotHeaderSchema(FileLineSchema):
    bank: str = Field(..., description="Bank identifier", example="104", min_length=3, max_length=3)
    lot: str = Field(..., description="Lot identifier", example="0001", min_length=4, max_length=4)
    registry_type: str = Field(..., description="Registry type", example="1", min_length=1, max_length=1)
    operation_type: str = Field(..., description="Operation type", example="C", min_length=1, max_length=1)
    service_type: str = Field(..., description="Service type", example="01", min_length=2, max_length=2)
    filler: str = Field(..., description="Filler", example=" " * 2, min_length=2, max_length=2)
    layout_version: str = Field(..., description="Layout version", example="010", min_length=3, max_length=3)
    filler_2: str = Field(..., description="Filler", example=" " * 1, min_length=1, max_length=1)
    inscription_type: str = Field(..., description="Inscription type", example="1", min_length=1, max_length=1)
    inscription_number: str = Field(
        ...,
        description="Inscription number",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    covenant: str = Field(..., description="Covenant", example="0" * 20, min_length=20, max_length=20)
    agency_code: str = Field(..., description="Agency code", example="00000", min_length=5, max_length=5)
    agency_vd: str = Field(..., description="Agency verification digit", example="0", min_length=1, max_length=1)
    account_number: str = Field(..., description="Account number", example="0" * 12, min_length=12, max_length=12)
    account_vd: str = Field(..., description="Account verification digit", example="0", min_length=1, max_length=1)
    agency_account_vd: str = Field(
        ...,
        description="Agency/Account verification digit",
        example="0",
        min_length=1,
        max_length=1,
    )
    enterprise_name: str = Field(..., description="Enterprise name", example="a" * 30, min_length=30, max_length=30)
    message: str = Field(..., description="Message", example="a" * 40, min_length=40, max_length=40)
    message_2: str = Field(..., description="Message 2", example="a" * 40, min_length=40, max_length=40)
    shipping_number: str = Field(..., description="Shipping number", example="0" * 8, min_length=8, max_length=8)
    record_date: str = Field(..., description="Record date", example="00000000", min_length=8, max_length=8)
    credit_date: str = Field(..., description="Credit date", example="00000000", min_length=8, max_length=8)
    model_code: str = Field(..., description="Model code", example="0" * 7, min_length=7, max_length=7)
    filler_3: str = Field(..., description="Filler", example=" " * 26, min_length=26, max_length=26)


class SegmentPSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "P",
        description="Segment name",
        example="P",
        min_length=1,
        max_length=1,
        regex="P",
    )
    bank: str = Field(..., description="Cod. do Banco na Compensacao", example="104", min_length=3, max_length=3)
    service_lot: str = Field(..., description="Lote de servico", example="0001", min_length=4, max_length=4)
    record_type: str = Field(..., description="Tipo de registro", example="3", min_length=1, max_length=1)
    record_number: str = Field(
        ...,
        description="Numero sequencial do registro no lote",
        example="00001",
        min_length=5,
        max_length=5,
    )
    segment_code: str = Field(
        ...,
        description="Codigo do segmento do registro detalhe",
        example="P",
        min_length=1,
        max_length=1,
    )
    filler: str = Field(..., description="Uso Exclusivo NEXXERA", example=" " * 1, min_length=1, max_length=1)
    remittance_movement_code: str = Field(
        ...,
        description="Codigo de movimento remessa",
        example="01",
        min_length=2,
        max_length=2,
    )
    maintaining_agency_code: str = Field(
        ...,
        description="Agencia mantenedora da conta",
        example="00000",
        min_length=5,
        max_length=5,
    )
    agency_dv: str = Field(..., description="Digito verificador da agencia", example="0", min_length=1, max_length=1)
    checking_account_number: str = Field(
        ...,
        description="Numero da conta corrente",
        example="0" * 12,
        min_length=12,
        max_length=12,
    )
    account_dv: str = Field(..., description="Digito verificador da conta", example="0", min_length=1, max_length=1)
    agency_account_dv: str = Field(
        ...,
        description="Digito verificador da agencia/conta",
        example="0",
        min_length=1,
        max_length=1,
    )
    our_number: str = Field(..., description="Nosso numero", example="0" * 20, min_length=20, max_length=20)
    wallet_code: str = Field(..., description="Codigo da carteira", example="1", min_length=1, max_length=1)
    registration_type: str = Field(..., description="Tipo de cadastramento", example="1", min_length=1, max_length=1)
    billing_document: str = Field(
        ...,
        description="Tipo de documento de cobranca",
        example="1",
        min_length=1,
        max_length=1,
    )
    billet_issue: str = Field(..., description="Emissao do bloqueto", example="1", min_length=1, max_length=1)
    billet_distribution: str = Field(
        ...,
        description="Distribuicao do bloqueto",
        example="0",
        min_length=1,
        max_length=1,
    )
    billing_document_number: str = Field(
        ...,
        description="Numero do documento de cobranca",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    due_date: str = Field(
        ...,
        description="Data de vencimento do titulo",
        example="00000000",
        min_length=8,
        max_length=8,
    )
    nominal_value: str = Field(
        ...,
        description="Valor nominal do titulo",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    collection_agency_code: str = Field(
        ...,
        description="Agencia cobradora",
        example="00000",
        min_length=5,
        max_length=5,
    )
    collection_agency_dv: str = Field(
        ...,
        description="Digito verificador da agencia cobradora",
        example="0",
        min_length=1,
        max_length=1,
    )
    species_code: str = Field(..., description="Especie do titulo", example="01", min_length=2, max_length=2)
    acceptance: str = Field(
        ...,
        description="Identificacao do titulo aceito/não aceito",
        example="N",
        min_length=1,
        max_length=1,
    )
    issuance_date: str = Field(
        ...,
        description="Data de emissao do titulo",
        example="00000000",
        min_length=8,
        max_length=8,
    )
    mora_interest_code: str = Field(..., description="Codigo do juros de mora", example="0", min_length=1, max_length=1)
    mora_interest_date: str = Field(
        ...,
        description="Data do juros de mora",
        example="00000000",
        min_length=8,
        max_length=8,
    )
    mora_interest_rate: str = Field(
        ...,
        description="Juros de mora por dia/taxa",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    discount_code: str = Field(..., description="Codigo do desconto 1", example="0", min_length=1, max_length=1)
    discount_date: str = Field(..., description="Data do desconto 1", example="00000000", min_length=8, max_length=8)
    discount_value: str = Field(
        ...,
        description="Valor/percentual a ser concedido",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    iof_value: str = Field(
        ...,
        description="Valor do IOF a ser recolhido",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    abatement_value: str = Field(..., description="Valor do abatimento", example="0" * 15, min_length=15, max_length=15)
    title_identification_in_company: str = Field(
        ...,
        description="Identificacao do titulo na empresa",
        example="0" * 25,
        min_length=25,
        max_length=25,
    )
    protest_code: str = Field(..., description="Codigo para protesto", example="0", min_length=1, max_length=1)
    protest_deadline: str = Field(..., description="Prazo para protesto", example="00", min_length=2, max_length=2)
    discharge_code: str = Field(..., description="Codigo para baixa/devolucao", example="0", min_length=1, max_length=1)
    discharge_deadline: str = Field(
        ...,
        description="Prazo para baixa/devolucao",
        example="000",
        min_length=3,
        max_length=3,
    )
    currency_code: str = Field(..., description="Codigo da moeda", example="00", min_length=2, max_length=2)
    credit_operation_contract_number: str = Field(
        ...,
        description="Numero do contrato da operacao de credito",
        example="0" * 10,
        min_length=10,
        max_length=10,
    )
    free_use: str = Field(..., description="Uso livre", example="N", min_length=1, max_length=1)

    class Config:
        load_only = ["segment_name"]


class SegmentQSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "Q",
        description="Segment name",
        example="Q",
        min_length=1,
        max_length=1,
        regex="Q",
    )
    bank_code: str = Field(..., description="Cod. do Banco na Compensacao", example="756", min_length=3, max_length=3)
    service_batch: str = Field(..., description="Lote de servico", example="0001", min_length=4, max_length=4)
    record_type: str = Field(..., description="Tipo de registro", example="3", min_length=1, max_length=1)
    record_number: str = Field(
        ...,
        description="Numero sequencial do registro no lote",
        example="00001",
        min_length=5,
        max_length=5,
    )
    segment_code: str = Field(
        ...,
        description="Codigo do segmento do registro detalhe",
        example="Q",
        min_length=1,
        max_length=1,
    )
    filler: str = Field(..., description="Uso Exclusivo NEXXERA", example=" ", min_length=1, max_length=1)
    transaction_code: str = Field(
        ...,
        description="Codigo de movimento remessa",
        example="01",
        min_length=2,
        max_length=2,
    )
    payee_type: str = Field(..., description="Tipo de inscricao", example="1", min_length=1, max_length=1)
    payee_number: str = Field(..., description="Numero de inscricao", example="0" * 15, min_length=15, max_length=15)
    payee_name: str = Field(..., description="Nome", example=" " * 40, min_length=40, max_length=40)
    payee_address: str = Field(..., description="Endereco", example=" " * 40, min_length=40, max_length=40)
    payee_district: str = Field(..., description="Bairro", example=" " * 15, min_length=15, max_length=15)
    payee_zip: str = Field(..., description="CEP", example="0" * 5, min_length=5, max_length=5)
    payee_zip_suffix: str = Field(..., description="Sufixo do CEP", example="0" * 3, min_length=3, max_length=3)
    payee_city: str = Field(..., description="Cidade", example=" " * 15, min_length=15, max_length=15)
    payee_state: str = Field(..., description="UF", example=" " * 2, min_length=2, max_length=2)
    guarantor_type: str = Field(
        ...,
        description="Tipo de inscricao do avalista",
        example="0",
        min_length=1,
        max_length=1,
    )
    guarantor_number: str = Field(
        ...,
        description="Numero de inscricao do avalista",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    guarantor_name: str = Field(..., description="Nome do avalista", example=" " * 40, min_length=40, max_length=40)
    corresponding_bank_code: str = Field(
        ...,
        description="Codigo do banco correspondente na compensacao",
        example="0" * 3,
        min_length=3,
        max_length=3,
    )
    corresponding_bank_our_number: str = Field(
        ...,
        description="Nosso numero no banco correspondente",
        example="0" * 20,
        min_length=20,
        max_length=20,
    )
    boleto_access: str = Field(..., description="Acesso ao boleto", example=" ", min_length=1, max_length=1)
    first_billing_instruction: str = Field(
        ...,
        description="Instrucao de cobranca 1",
        example=" " * 2,
        min_length=2,
        max_length=2,
    )
    second_billing_instruction: str = Field(
        ...,
        description="Instrucao de cobranca 2",
        example=" " * 2,
        min_length=2,
        max_length=2,
    )
    wallet_variation: str = Field(..., description="Variacao da carteira", example=" " * 3, min_length=3, max_length=3)

    class Config:
        load_only = ["segment_name"]


class SegmentRSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "R",
        description="Segment name",
        example="R",
        min_length=1,
        max_length=1,
        regex="R",
    )

    class Config:
        load_only = ["segment_name"]


class SegmentSSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "S",
        description="Segment name",
        example="S",
        min_length=1,
        max_length=1,
        regex="S",
    )

    class Config:
        load_only = ["segment_name"]


class SegmentTSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "T",
        description="Segment name",
        example="T",
        min_length=1,
        max_length=1,
        regex="T",
    )
    bank: str = Field(..., description="Cod. do Banco na Compensacao", example="104", min_length=3, max_length=3)
    service_lot: str = Field(..., description="Lote de servico", example="0001", min_length=4, max_length=4)
    record_type: str = Field(..., description="Tipo de registro", example="3", min_length=1, max_length=1)
    record_number: str = Field(
        ...,
        description="Numero sequencial do registro no lote",
        example="00001",
        min_length=5,
        max_length=5,
    )
    segment_code: str = Field(
        ...,
        description="Codigo do segmento do registro detalhe",
        example="T",
        min_length=1,
        max_length=1,
    )
    filler: str = Field(..., description="Uso Exclusivo NEXXERA", example=" " * 1, min_length=1, max_length=1)
    return_movement_code: str = Field(
        ...,
        description="Codigo de movimento retorno",
        example="01",
        min_length=2,
        max_length=2,
    )
    maintaining_agency_code: str = Field(
        ...,
        description="Agencia mantenedora da conta",
        example="00000",
        min_length=5,
        max_length=5,
    )
    agency_dv: str = Field(..., description="Digito verificador da agencia", example="0", min_length=1, max_length=1)
    checking_account_number: str = Field(
        ...,
        description="Numero da conta corrente",
        example="0" * 12,
        min_length=12,
        max_length=12,
    )
    account_dv: str = Field(..., description="Digito verificador da conta", example="0", min_length=1, max_length=1)
    agency_account_dv: str = Field(
        ...,
        description="Digito verificador da agencia/conta",
        example="0",
        min_length=1,
        max_length=1,
    )
    our_number: str = Field(..., description="Nosso numero", example="0" * 20, min_length=20, max_length=20)
    wallet_code: str = Field(..., description="Codigo da carteira", example="1", min_length=1, max_length=1)
    billing_document_number: str = Field(
        ...,
        description="Numero do documento de cobranca",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    due_date: str = Field(
        ...,
        description="Data de vencimento do titulo",
        example="00000000",
        min_length=8,
        max_length=8,
    )
    nominal_value: str = Field(
        ...,
        description="Valor nominal do titulo",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    bank_number: str = Field(
        ...,
        description="Numero do banco cobrador",
        example="0" * 3,
        min_length=3,
        max_length=3,
    )
    collection_agency_code: str = Field(
        ...,
        description="Agencia cobradora",
        example="00000",
        min_length=5,
        max_length=5,
    )
    collection_agency_dv: str = Field(
        ...,
        description="Digito verificador da agencia cobradora",
        example="0",
        min_length=1,
        max_length=1,
    )
    enterprise_use: str = Field(
        ...,
        description="Uso da empresa",
        example=" " * 25,
        min_length=25,
        max_length=25,
    )
    currency_code: str = Field(
        ...,
        description="Codigo da moeda",
        example="09",
        min_length=2,
        max_length=2,
    )
    payee_type: str = Field(
        ...,
        description="Tipo de inscricao",
        example="1",
        min_length=1,
        max_length=1,
    )
    payee_number: str = Field(
        ...,
        description="Numero de inscricao",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    payee_name: str = Field(
        ...,
        description="Nome",
        example=" " * 40,
        min_length=40,
        max_length=40,
    )
    contract_number: str = Field(
        ...,
        description="Numero do contrato",
        example=" " * 10,
        min_length=10,
        max_length=10,
    )
    tax_value: str = Field(
        ...,
        description="Valor das tarifas/custos",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )
    ocurrency_description: str = Field(
        ...,
        description="Motivo da ocorrencia para retorno",
        example=" " * 10,
        min_length=10,
        max_length=10,
    )
    filler_1: str = Field(
        ...,
        description="Uso Exclusivo NEXXERA",
        example=" " * 14,
        min_length=14,
        max_length=14,
    )
    variation_code: str = Field(
        ...,
        description="Codigo da variacao carteira",
        example="000",
        min_length=3,
        max_length=3,
    )

    class Config:
        load_only = ["segment_name"]


class SegmentUSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "U",
        description="Segment name",
        example="U",
        min_length=1,
        max_length=1,
        regex="U",
    )
    bank: str = Field(
        ...,
        description="Cod. do Banco na Compensacao",
        example="104",
        min_length=3,
        max_length=3,
    )
    service_lot: str = Field(
        ...,
        description="Lote de servico",
        example="0001",
        min_length=4,
        max_length=4,
    )
    record_type: str = Field(
        ...,
        description="Tipo de registro",
        example="3",
        min_length=1,
        max_length=1,
    )
    record_number: str = Field(
        ...,
        description="Numero sequencial do registro no lote",
        example="00001",
        min_length=5,
        max_length=5,
    )
    segment_code: str = Field(
        ...,
        description="Codigo do segmento do registro detalhe",
        example="U",
        min_length=1,
        max_length=1,
    )
    filler: str = Field(
        ...,
        description="Uso Exclusivo NEXXERA",
        example=" " * 1,
        min_length=1,
        max_length=1,
    )
    return_movement_code: str = Field(
        ...,
        description="Codigo de movimento retorno",
        example="01",
        min_length=2,
        max_length=2,
    )

    title_accruals: str = Field(
        ...,
        description="Valor dos juros / multa / encargos",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    title_discount: str = Field(
        ...,
        description="Valor do desconto concedido",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    title_rebate: str = Field(
        ...,
        description="Valor do abatimento concedido",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    title_iof: str = Field(
        ...,
        description="Valor do IOF recolhido",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    title_paid: str = Field(
        ...,
        description="Valor pago pelo sacado",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    title_liquid: str = Field(
        ...,
        description="Valor liquido a ser creditado",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    other_costs: str = Field(
        ...,
        description="Valor de outras despesas",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    other_credits: str = Field(
        ...,
        description="Valor de outros creditos",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    ocurrence_date: str = Field(
        ...,
        description="Data da ocorrencia",
        example="0" * 8,
        min_length=8,
        max_length=8,
    )

    credit_date: str = Field(
        ...,
        description="Data do credito",
        example="0" * 8,
        min_length=8,
        max_length=8,
    )

    withdrawn_occurrence_code: str = Field(
        ...,
        description="Codigo da ocorrencia do sacado",
        example="0" * 4,
        min_length=4,
        max_length=4,
    )

    withdrawn_occurrence_date: str = Field(
        ...,
        description="Data da ocorrencia do sacado",
        example="0" * 8,
        min_length=8,
        max_length=8,
    )

    withdrawn_occurrence_value: str = Field(
        ...,
        description="Valor da ocorrencia do sacado",
        example="0" * 15,
        min_length=15,
        max_length=15,
    )

    withdrawn_occurrence_complement: str = Field(
        ...,
        description="Complemento da ocorrencia do sacado",
        example="0" * 30,
        min_length=30,
        max_length=30,
    )

    corresponding_bank_code: str = Field(
        ...,
        description="Código do banco correspondente",
        example="0" * 3,
        min_length=3,
        max_length=3,
    )

    corresponding_bank_our_number: str = Field(
        ...,
        description="Nosso numero no banco correspondente",
        example="0" * 20,
        min_length=20,
        max_length=20,
    )

    filler_1: str = Field(
        ...,
        description="Uso Exclusivo NEXXERA",
        example=" " * 7,
        min_length=7,
        max_length=7,
    )

    class Config:
        load_only = ["segment_name"]


class SegmentVSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "V",
        description="Segment name",
        example="V",
        min_length=1,
        max_length=1,
        regex="V",
    )

    class Config:
        load_only = ["segment_name"]


class SegmentWSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "W",
        description="Segment name",
        example="W",
        min_length=1,
        max_length=1,
        regex="W",
    )

    class Config:
        load_only = ["segment_name"]


class SegmentYSchema(FileLineSchema):
    segment_name: Optional[str] = Field(
        "Y",
        description="Segment name",
        example="Y",
        min_length=1,
        max_length=1,
        regex="Y",
    )

    class Config:
        load_only = ["segment_name"]


class LotTrailerSchema(FileLineSchema):
    bank_code: str = Field(..., description="Cod. do Banco na Compensacao", example="104", min_length=3, max_length=3)
    batch: str = Field(..., description="Lote de servico", example="0000", min_length=4, max_length=4)
    record_type: str = Field(..., description="Tipo de registro", example="5", min_length=1, max_length=1, regex="5")
    filler: str = Field(..., description="Uso Exclusivo FEBRABAN/CNAB", example=" " * 9, min_length=9, max_length=9)
    batch_records_quantity: str = Field(
        ...,
        description="Quantidade de registros do lote",
        example="000000",
        min_length=6,
        max_length=6,
    )
    simple_billing_quantity: str = Field(
        ...,
        description="Quantidade de titulos em cobranca simples",
        example="000000",
        min_length=6,
        max_length=6,
    )
    simple_billing_value: str = Field(
        ...,
        description="Valor total dos titulos em cobranca simples",
        example=" " * 17,
        min_length=17,
        max_length=17,
    )
    linked_billing_quantity: str = Field(
        ...,
        description="Quantidade de titulos em cobranca vinculada",
        example="000000",
        min_length=6,
        max_length=6,
    )
    linked_billing_value: str = Field(
        ...,
        description="Valor total dos titulos em cobranca vinculada",
        example=" " * 17,
        min_length=17,
        max_length=17,
    )
    pledged_billing_quantity: str = Field(
        ...,
        description="Quantidade de titulos em cobranca caucionada",
        example="000000",
        min_length=6,
        max_length=6,
    )
    pledged_billing_value: str = Field(
        ...,
        description="Valor total dos titulos em cobranca caucionada",
        example=" " * 17,
        min_length=17,
        max_length=17,
    )
    discounted_billing_quantity: str = Field(
        ...,
        description="Quantidade de titulos em cobranca descontada",
        example="000000",
        min_length=6,
        max_length=6,
    )
    discounted_billing_value: str = Field(
        ...,
        description="Valor total dos titulos em cobranca descontada",
        example=" " * 17,
        min_length=17,
        max_length=17,
    )
    launch_notice_number: str = Field(
        ...,
        description="Numero do aviso de lancamento",
        example=" " * 8,
        min_length=8,
        max_length=8,
    )
    filler_2: str = Field(..., description="Uso Exclusivo NEXXERA", example=" " * 117, min_length=117, max_length=117)


class ShippingFileSchema(BaseModel):
    header_file: FileHeaderSchema
    header_lot: LotHeaderSchema
    segments: List[
        Union[
            SegmentPSchema,
            SegmentQSchema,
            SegmentRSchema,
            SegmentSSchema,
            SegmentYSchema,
            SegmentVSchema,
        ]
    ]
    trailer_lot: LotTrailerSchema
    trailer_file: FileTrailerSchema


class ReturnFileSchema(BaseModel):
    header_file: FileHeaderSchema
    header_lot: LotHeaderSchema
    segments: List[
        Union[
            SegmentTSchema,
            SegmentUSchema,
            SegmentWSchema,
            SegmentYSchema,
        ]
    ]
    trailer_lot: LotTrailerSchema
    trailer_file: FileTrailerSchema
