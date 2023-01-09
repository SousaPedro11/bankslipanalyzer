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
        elif re.match(validators.regex_segment_nexxera(), line):
            self.__generate_segment(line_number, line, shipping)
        elif re.match(validators.regex_lot_trailer_nexxera(), line):
            self.__generate_lot_trailer(line_number, line, shipping)
        elif re.match(validators.regex_file_trailer_nexxera(), line):
            self.__generate_file_trailer(line_number, line, shipping)

        print(shipping)

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
        pass

    def __generate_segment(self, line_number: int, line, shipping):
        groups = None
        segment = None
        if re.match(validators.regex_p_segment_nexxera(), line):
            groups = re.match(validators.regex_p_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentPSchema()
        elif re.match(validators.regex_q_segment_nexxera(), line):
            groups = re.match(validators.regex_q_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentQSchema()
        elif re.match(validators.regex_r_segment_nexxera(), line):
            groups = re.match(validators.regex_r_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentRSchema()
        elif re.match(validators.regex_s_segment_nexxera(), line):
            groups = re.match(validators.regex_s_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentSSchema()
        elif re.match(validators.regex_v_segment_nexxera(), line):
            groups = re.match(validators.regex_v_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentVSchema()
        elif re.match(validators.regex_y_segment_nexxera(), line):
            groups = re.match(validators.regex_y_segment_nexxera(), line).groupdict()
            segment = shipping_schema.SegmentYSchema()

        return groups, segment

    def __generate_lot_trailer(self, line_number: int, line, shipping):
        pass
