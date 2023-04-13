import re
from abc import ABC, abstractmethod
from typing import List

from app.api.helpers import validators
from app.api.schemas import nexxera_document


class BaseDocumentService(ABC):
    def __init__(self):
        self.content: List[str] = []

    def __set_attributes(self):
        document = {
            "header_file": None,
            "header_lot": None,
            "segments": [],
            "trailer_lot": None,
            "trailer_file": None,
        }

        for index, line in enumerate(self.content):
            self._set_document_attribute(index + 1, line, document)

        return document

    def _set_document_attribute(self, line_number: int, line: str, document: dict):
        if re.match(validators.regex_file_header_nexxera(), line):
            self.__generate_file_header(line_number, line, document)
        elif re.match(validators.regex_lot_header_nexxera(), line):
            self.__generate_lot_header(line_number, line, document)
        elif re.match(validators.regex_lot_trailer_nexxera(), line):
            self.__generate_lot_trailer(line_number, line, document)
        elif re.match(validators.regex_file_trailer_nexxera(), line):
            self.__generate_file_trailer(line_number, line, document)

    def __generate_file_trailer(self, line_number: int, line, document):
        groups = re.match(validators.regex_file_trailer_nexxera(), line).groupdict()
        document["trailer_file"] = nexxera_document.FileTrailerSchema(
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

    def __generate_file_header(self, line_number: int, line, document):
        groups = re.match(validators.regex_file_header_nexxera(), line).groupdict()
        document["header_file"] = nexxera_document.FileHeaderSchema(
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

    def get_bank_slip_shipping_return(self, content: str):
        self.content = content.splitlines()

        segments = self.__set_attributes()
        return segments

    def __generate_lot_header(self, line_number: int, line, document):
        groups = re.match(validators.regex_lot_header_nexxera(), line).groupdict()
        document["header_lot"] = nexxera_document.LotHeaderSchema(
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

    @abstractmethod
    def _generate_segment(self, line_number: int, line, document):
        raise NotImplementedError

    def __generate_lot_trailer(self, line_number: int, line, document):
        groups = re.match(validators.regex_lot_trailer_nexxera(), line).groupdict()
        document["trailer_lot"] = nexxera_document.LotTrailerSchema(
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
