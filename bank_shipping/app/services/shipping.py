import re
from typing import List

from app.api.helpers import validators
from app.api.schemas import shipping as shipping_schema


class BankSlipShippingService:
    def __init__(self):
        self.content: List[str] = []

    def __set_attributes(self):
        shipping = {
            "header_file": None,
            "header_lot": None,
            "shippings": [],
            "trailer_lot": None,
            "trailer_file": None,
        }

        for index, line in enumerate(self.content):
            self.__set_shipping_attribute(index + 1, line, shipping)

        return shipping

    def __set_shipping_attribute(self, line_number: int, line: str, shipping: dict):
        if re.match(validators.regex_file_header_nexxera(), line):
            self.__generate_file_header(line_number, line, shipping)
        elif re.match(validators.regex_lot_header_nexxera(), line):
            self.__generate_lot_header(line_number, line, shipping)
        elif validators.is_segment_nexxera(line):
            self.__generate_segment(line_number, line, shipping)
        elif re.match(validators.regex_lot_trailer_nexxera(), line):
            self.__generate_lot_trailer(line_number, line, shipping)
        elif re.match(validators.regex_file_trailer_nexxera(), line):
            self.__generate_file_trailer(line_number, line, shipping)

    def __generate_file_trailer(self, line_number: int, line, shipping):
        groups = re.match(validators.regex_file_trailer_nexxera(), line).groupdict()
        shipping["trailer_file"] = shipping_schema.FileTrailerSchema(
            bank=groups["banco"],
            lot=groups["lote"],
            registry_type=groups["registro"],
            filler=groups["filler"],
            total_lots=groups["qtd_lotes"],
            total_registries=groups["qtd_registros"],
            total_accounts=groups["qtd_contas"],
            filler_2=groups["filler_2"],
            file_line=line_number,
        )

    def __generate_file_header(self, line_number: int, line, shipping):
        groups = re.match(validators.regex_file_header_nexxera(), line).groupdict()
        shipping["header_file"] = shipping_schema.FileHeaderSchema(
            file_line=line_number,
            bank=groups["banco"],
            lot=groups["lote"],
            registry_type=groups["registro"],
            filler=groups["filler"],
            inscription_type=groups["inscricao_tipo"],
            inscription_number=groups["inscricao_numero"],
            covenant=groups["convenio"],
            agency_code=groups["agencia_codigo"],
            agency_vd=groups["agencia_dv"],
            account_number=groups["conta_numero"],
            account_vd=groups["conta_dv"],
            agency_account_vd=groups["ag_conta_dv"],
            enterprise_name=groups["empresa_nome"],
            bank_name=groups["banco_nome"],
            van_name=groups["van_nome"],
            file_code=groups["arquivo_codigo"],
            file_generation_date=groups["arquivo_geracao_data"],
            file_generation_hour=groups["arquivo_geracao_hora"],
            file_sequential_number=groups["arquivo_sequencia"],
            file_layout_version=groups["arquivo_layout"],
            file_density=groups["arquivo_densidade"],
            bank_reserved=groups["reservado_banco"],
            enterprise_reserved=groups["reservado_empresa"],
            bank_observations=groups["observacoes"],
        )

    def get_bank_slip_shipping(self, content: str):
        self.content = content.splitlines()

        shippings = self.__set_attributes()
        return shippings

    def __generate_lot_header(self, line_number: int, line, shipping):
        groups = re.match(validators.regex_lot_header_nexxera(), line).groupdict()
        shipping["header_lot"] = shipping_schema.LotHeaderSchema(
            file_line=line_number,
            bank=groups["banco"],
            lot=groups["lote"],
            registry_type=groups["registro"],
            operation_type=groups["operacao"],
            service_type=groups["servico"],
            filler=groups["filler"],
            layout_version=groups["versao_layout"],
            filler_2=groups["filler_2"],
            inscription_type=groups["inscricao_tipo"],
            inscription_number=groups["inscricao_numero"],
            covenant=groups["convenio"],
            agency_code=groups["agencia_codigo"],
            agency_vd=groups["agencia_dv"],
            account_number=groups["conta_numero"],
            account_vd=groups["conta_dv"],
            agency_account_vd=groups["ag_conta_dv"],
            enterprise_name=groups["empresa_nome"],
            message=groups["mensagem"],
            message_2=groups["mensagem_2"],
            shipping_number=groups["numero_remessa"],
            record_date=groups["data_gravacao"],
            credit_date=groups["data_credito"],
            model_code=groups["modelo_cod"],
            filler_3=groups["filler_3"],
        )

    def __generate_segment(self, line_number: int, line, shipping):
        groups = None
        segment = None
        if re.match(validators.regex_p_segment_nexxera(), line):
            groups = re.match(validators.regex_p_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentPSchema(
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
            segment = shipping_schema.SegmentQSchema(
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
            segment = shipping_schema.SegmentRSchema(file_line=line_number)
        elif re.match(validators.regex_s_segment_nexxera(), line):
            groups = re.match(validators.regex_s_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentSSchema(file_line=line_number)
        elif re.match(validators.regex_v_segment_nexxera(), line):
            groups = re.match(validators.regex_v_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentVSchema(file_line=line_number)
        elif re.match(validators.regex_y_segment_nexxera(), line):
            groups = re.match(validators.regex_y_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentYSchema(file_line=line_number)

        if segment:
            shipping["shippings"].append(segment)

    def __generate_lot_trailer(self, line_number: int, line, shipping):
        groups = re.match(validators.regex_lot_trailer_nexxera(), line).groupdict()
        shipping["trailer_lot"] = shipping_schema.LotTrailerSchema(
            file_line=line_number,
            bank_code=groups["banco"],
            batch=groups["lote"],
            record_type=groups["registro"],
            filler=groups["filler"],
            batch_records_quantity=groups["qtd_registros_lote"],
            simple_billing_quantity=groups["cobranca_simples_qtd"],
            simple_billing_value=groups["cobranca_simples_valor"],
            linked_billing_quantity=groups["cobranca_vinculada_qtd"],
            linked_billing_value=groups["cobranca_vinculada_valor"],
            pledged_billing_quantity=groups["cobranca_caucionada_qtd"],
            pledged_billing_value=groups["cobranca_caucionada_valor"],
            discounted_billing_quantity=groups["cobranca_descontada_qtd"],
            discounted_billing_value=groups["cobranca_descontada_valor"],
            launch_notice_number=groups["aviso_numero"],
            filler_2=groups["filler_2"],
        )
