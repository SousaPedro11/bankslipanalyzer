import re

from app.api.helpers import validators
from app.api.schemas import nexxera_document
from app.services.abstract.nexxera import BaseDocumentService


class BankSlipReturnNexxeraService(BaseDocumentService):
    def _set_document_attribute(self, line_number: int, line: str, document: dict):
        super()._set_document_attribute(line_number, line, document)

        if validators.is_return_segment_nexxera(line):
            self._generate_segment(line_number, line, document)

    def _generate_segment(self, line_number: int, line, document):
        segment = None
        if re.match(validators.regex_t_segment_nexxera(), line):
            groups = re.match(validators.regex_t_segment_nexxera(), line).groupdict()
            segment = nexxera_document.SegmentTSchema(
                file_line=line_number,
                bank=groups["banco"],
                service_lot=groups["lote"],
                record_type=groups["registro"],
                record_number=groups["numero_registro"],
                segment_code=groups["segmento"],
                filler=groups["filler"],
                return_movement_code=groups["movimento_codigo"],
                maintaining_agency_code=groups["agencia_codigo"],
                agency_dv=groups["agencia_dv"],
                checking_account_number=groups["conta_numero"],
                account_dv=groups["conta_dv"],
                agency_account_dv=groups["agencia_conta_dv"],
                our_number=groups["nosso_numero"],
                wallet_code=groups["carteira_codigo"],
                billing_document_number=groups["documento_numero"],
                due_date=groups["vencimento_data"],
                nominal_value=groups["valor"],
                bank_number=groups["banco_recebedor_codigo"],
                collection_agency_code=groups["agencia_recebedora_codigo"],
                collection_agency_dv=groups["agencia_recebedora_dv"],
                enterprise_use=groups["exclusivo_empresa"],
                currency_code=groups["moeda_codigo"],
                payee_type=groups["sacado_tipo_inscricao"],
                payee_number=groups["sacado_numero_inscricao"],
                payee_name=groups["sacado_nome"],
                contract_number=groups["contrato_numero"],
                tax_value=groups["tarifa_valor"],
                ocurrency_description=groups["ocorrencia_motivo"],
                filler_1=groups["filler_1"],
                variation_code=groups["variacao_carteira_codigo"],
            )
        elif re.match(validators.regex_u_segment_nexxera(), line):
            groups = re.match(validators.regex_u_segment_nexxera(), line).groupdict()

            segment = nexxera_document.SegmentUSchema(
                file_line=line_number,
                bank=groups["banco"],
                service_lot=groups["lote"],
                record_type=groups["registro"],
                record_number=groups["numero_registro"],
                segment_code=groups["segmento"],
                filler=groups["filler"],
                return_movement_code=groups["movimento_codigo"],
                title_accruals=groups["titulo_acrescimos"],
                title_discount=groups["titulo_desconto"],
                title_rebate=groups["titulo_abatimento"],
                title_iof=groups["titulo_iof"],
                title_paid=groups["titulo_pago"],
                title_liquid=groups["titulo_liquido"],
                other_costs=groups["outros_custos"],
                other_credits=groups["outros_creditos"],
                ocurrence_date=groups["data_ocorrencia"],
                credit_date=groups["data_credito"],
                withdrawn_occurrence_code=groups["sacado_ocorrencia_codigo"],
                withdrawn_occurrence_date=groups["sacado_ocorrencia_data"],
                withdrawn_occurrence_value=groups["sacado_ocorrencia_valor"],
                withdrawn_occurrence_complement=groups["sacado_ocorrencia_complemento"],
                corresponding_bank_code=groups["banco_correspondente_codigo"],
                corresponding_bank_our_number=groups["banco_correspondente_nosso_numero"],
                filler_1=groups["filler_1"],
            )

        if segment:
            document["segments"].append(segment)
