import re

from app.api.helpers import validators
from app.api.schemas import nexxera_document
from app.services.abstract.nexxera import BaseDocumentService


class BankSlipShippingService(BaseDocumentService):
    def _set_document_attribute(self, line_number: int, line: str, document: dict):
        super()._set_document_attribute(line_number, line, document)

        if validators.is_shipping_segment_nexxera(line):
            self._generate_segment(line_number, line, document)

    def _generate_segment(self, line_number: int, line, document):
        segment = None
        if re.match(validators.regex_p_segment_nexxera(), line):
            groups = re.match(validators.regex_p_segment_nexxera(), line).groupdict()
            segment = nexxera_document.SegmentPSchema(
                file_line=line_number,
                bank=groups["banco"],
                service_lot=groups["lote"],
                record_type=groups["registro"],
                record_number=groups["numero_registro"],
                segment_code=groups["segmento"],
                filler=groups["filler"],
                remittance_movement_code=groups["movimento_codigo"],
                maintaining_agency_code=groups["agencia_codigo"],
                agency_dv=groups["agencia_dv"],
                checking_account_number=groups["conta_numero"],
                account_dv=groups["conta_dv"],
                agency_account_dv=groups["ag_conta_dv"],
                our_number=groups["nosso_numero"],
                wallet_code=groups["carteira_codigo"],
                registration_type=groups["cadastramento"],
                billing_document=groups["documento"],
                billet_issue=groups["emissao_bloqueto"],
                billet_distribution=groups["distribuicao_bloqueto"],
                billing_document_number=groups["documento_numero"],
                due_date=groups["vencimento"],
                nominal_value=groups["valor"],
                collection_agency_code=groups["agencia_cobranca_codigo"],
                collection_agency_dv=groups["agencia_cobranca_dv"],
                species_code=groups["especie_codigo"],
                acceptance=groups["aceite"],
                issuance_date=groups["emissao"],
                mora_interest_code=groups["juros_mora_codigo"],
                mora_interest_date=groups["juros_mora_data"],
                mora_interest_rate=groups["juros_mora_taxa"],
                discount_code=groups["desconto_codigo"],
                discount_date=groups["desconto_data"],
                discount_value=groups["desconto_valor"],
                iof_value=groups["valor_iof"],
                abatement_value=groups["valor_abatimento"],
                title_identification_in_company=groups["identificacao_titulo_empresa"],
                protest_code=groups["codigo_protesto"],
                protest_deadline=groups["prazo_protesto"],
                discharge_code=groups["codigo_baixa"],
                discharge_deadline=groups["prazo_baixa"],
                currency_code=groups["moeda_codigo"],
                credit_operation_contract_number=groups["contrato_numero"],
                free_use=groups["uso_livre"],
            )
        elif re.match(validators.regex_q_segment_nexxera(), line):
            groups = re.match(validators.regex_q_segment_nexxera(), line).groupdict()
            segment = nexxera_document.SegmentQSchema(
                file_line=line_number,
                bank_code=groups["banco"],
                service_batch=groups["lote"],
                record_type=groups["registro"],
                record_number=groups["numero_registro"],
                segment_code=groups["segmento"],
                filler=groups["filler"],
                transaction_code=groups["movimento_codigo"],
                payee_type=groups["sacado_inscricao_tipo"],
                payee_number=groups["sacado_inscricao_numero"],
                payee_name=groups["sacado_nome"],
                payee_address=groups["sacado_endereco"],
                payee_district=groups["sacado_bairro"],
                payee_zip=groups["sacado_cep"],
                payee_zip_suffix=groups["sacado_cep_sufixo"],
                payee_city=groups["sacado_cidade"],
                payee_state=groups["sacado_uf"],
                guarantor_type=groups["avalista_inscricao_tipo"],
                guarantor_number=groups["avalista_inscricao_numero"],
                guarantor_name=groups["avalista_nome"],
                corresponding_bank_code=groups["banco_correspondente_codigo"],
                corresponding_bank_our_number=groups["banco_correspondente_nosso_numero"],
                boleto_access=groups["acesso_boleto"],
                first_billing_instruction=groups["instrucao_cobranca_primeira"],
                second_billing_instruction=groups["instrucao_cobranca_segunda"],
                wallet_variation=groups["variacao_carteira"],
            )
        elif re.match(validators.regex_r_segment_nexxera(), line):
            groups = re.match(validators.regex_r_segment_nexxera(), line).groupdict()
            segment = nexxera_document.SegmentRSchema(file_line=line_number)
        elif re.match(validators.regex_s_segment_nexxera(), line):
            groups = re.match(validators.regex_s_segment_nexxera(), line).groupdict()
            segment = nexxera_document.SegmentSSchema(file_line=line_number)
        elif re.match(validators.regex_v_segment_nexxera(), line):
            groups = re.match(validators.regex_v_segment_nexxera(), line).groupdict()
            segment = nexxera_document.SegmentVSchema(file_line=line_number)
        elif re.match(validators.regex_y_segment_nexxera(), line):
            groups = re.match(validators.regex_y_segment_nexxera(), line).groupdict()
            segment = nexxera_document.SegmentYSchema(file_line=line_number)

        if segment:
            document["segments"].append(segment)
