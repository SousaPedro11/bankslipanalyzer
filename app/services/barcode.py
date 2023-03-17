import re
from functools import lru_cache
from typing import Optional

from app.api.helpers.calculators import due_date_from_factor, module_11
from app.api.helpers.validators import regex_barcode
from app.api.schemas.bank_slip import BarcodeOutputSchema, BarcodeSchema


class BarcodeService:
    def __init__(self):
        self.original_barcode: Optional[BarcodeSchema] = None
        self.barcode: Optional[BarcodeOutputSchema] = None

    def __get_original_barcode_object(self, barcode):
        groups = re.match(regex_barcode(), barcode).groupdict()

        return BarcodeSchema(
            bank=groups["banco"],
            currency_code=groups["codigo_moeda"],
            due_date_factor=groups["fator_vencimento"],
            document_value=groups["valor_documento"],
            beneficiary_code=groups["codigo_beneficiario"],
            sequence_1=groups["sequencia_1"],
            constant_1=groups["constante_1"],
            sequence_2=groups["sequencia_2"],
            constant_2=groups["constante_2"],
            sequence_3=groups["sequencia_3"],
            vd_general=groups["dv_geral"],
            vd_field_free=groups["dv_campo_livre"],
        )

    def _calculate_beneficiary_code_verification_digit(self):
        beneficiary_code = self.original_barcode.beneficiary_code
        dv_beneficiary_code = None
        if beneficiary_code.endswith("0") and int(beneficiary_code[:-1]) <= 999999:
            beneficiary_code = beneficiary_code[:-1]
            dv_beneficiary_code = module_11(beneficiary_code)

        elif int(beneficiary_code) <= 999999 and not beneficiary_code.endswith("0"):
            beneficiary_code = str(int(beneficiary_code[:-1])).zfill(6)
            dv_beneficiary_code = module_11(beneficiary_code)

        beneficiary_code = (
            beneficiary_code if dv_beneficiary_code is None else f"{beneficiary_code}{dv_beneficiary_code}"
        )
        return beneficiary_code

    @lru_cache
    def _calculate_general_verification_digit(self):
        beneficiary_code = self._calculate_beneficiary_code_verification_digit()
        return module_11(
            "".join(
                [
                    self.barcode.bank,
                    self.barcode.currency_code,
                    self.barcode.due_date_factor,
                    self.barcode.document_value,
                    beneficiary_code,
                    self.barcode.sequence_1,
                    self.barcode.constant_1,
                    self.barcode.sequence_2,
                    self.barcode.constant_2,
                    self.barcode.sequence_3,
                    self.barcode.vd_field_free,
                ],
            ),
            general=True,
        )

    @lru_cache
    def _calculate_field_free_verification_digit(self):
        beneficiary_code = self._calculate_beneficiary_code_verification_digit()
        return module_11(
            "".join(
                [
                    beneficiary_code,
                    self.barcode.sequence_1,
                    self.barcode.constant_1,
                    self.barcode.sequence_2,
                    self.barcode.constant_2,
                    self.barcode.sequence_3,
                ],
            ),
        )

    @lru_cache
    def _get_due_date(self):
        return due_date_from_factor(self.barcode.due_date_factor)

    def validate(self, barcode: str):
        from app.services.digitable_line import DigitableLineService

        self.original_barcode = self.__get_original_barcode_object(barcode)
        self.barcode = BarcodeOutputSchema(**self.original_barcode.dict())

        self.barcode.expected_barcode = self.original_barcode
        self.barcode.expected_barcode.vd_general = None
        self.barcode.expected_barcode.vd_field_free = None

        self.barcode.expected_barcode.vd_field_free = str(
            self._calculate_field_free_verification_digit(),
        )
        self.barcode.expected_barcode.vd_general = str(
            self._calculate_general_verification_digit(),
        )
        self.barcode.due_date = self._get_due_date()

        self.barcode.expected_digitable_line = DigitableLineService().get_digitable_line_by_barcode(
            self.barcode.expected_barcode,
        )

        return self.barcode
