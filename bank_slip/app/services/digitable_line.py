import re
from typing import List, Optional

from app.api.helpers.calculators import module_10
from app.api.helpers.validators import regex_digitable_line
from app.api.schemas.bank_slip import BarcodeSchema, DigitableLineOutputSchema, DigitableLineSchema


class DigitableLineService:
    def __init__(self) -> None:
        self.original_digitable_line: Optional[DigitableLineSchema] = None
        self.digitable_line: Optional[DigitableLineOutputSchema] = None

    def __get_original_digitable_line_object(self, digitable_line):
        digitable_line = digitable_line.replace(" ", "").replace(".", "")
        groups = re.match(regex_digitable_line(), digitable_line).groupdict()
        return DigitableLineSchema(
            field_1=groups["campo_1"],
            field_2=groups["campo_2"],
            field_3=groups["campo_3"],
            field_4=groups["campo_4"],
            field_5=groups["campo_5"],
        )

    def _generate_field_x(self, field_content: List, dot_position: int):
        field_x_verification_digit = str(
            self._calculate_field_x_verification_digit("".join(field_content)),
        )
        field_content.append(field_x_verification_digit)
        field_content = "".join(field_content)
        return f"{field_content[:dot_position]}.{field_content[dot_position:]}"

    def get_digitable_line_by_barcode(self, barcode: BarcodeSchema):
        field_1 = self._generate_field_x(
            [
                barcode.bank,
                barcode.currency_code,
                barcode.beneficiary_code[0],
                barcode.beneficiary_code[1:5],
            ],
            5,
        )
        field_2 = self._generate_field_x(
            [
                barcode.beneficiary_code[5:],
                barcode.sequence_1,
                barcode.constant_1,
                barcode.sequence_2,
                barcode.constant_2,
            ],
            5,
        )

        field_3 = self._generate_field_x(
            [
                barcode.sequence_3,
                barcode.vd_field_free,
            ],
            5,
        )

        return DigitableLineSchema(
            field_1=field_1,
            field_2=field_2,
            field_3=field_3,
            field_4=barcode.vd_general,
            field_5=f"{barcode.due_date_factor}{barcode.document_value}",
        )

    def validate(self, digitable_line: str):
        self.original_digitable_line = self.__get_original_digitable_line_object(
            digitable_line,
        )
        self.digitable_line = DigitableLineOutputSchema(**self.original_digitable_line.dict())
        self.digitable_line.barcode = self.get_barcode_by_digitable_line(
            self.original_digitable_line,
        )

        return self.digitable_line

    def _calculate_field_x_verification_digit(self, digits):
        return module_10(digits)

    def get_barcode_by_digitable_line(self, digitable_line: DigitableLineSchema):
        from bank_slip.app.services.barcode import BarcodeService

        field_1 = digitable_line.field_1.replace(".", "")
        field_2 = digitable_line.field_2.replace(".", "")
        field_3 = digitable_line.field_3.replace(".", "")

        barcode_components = [
            field_1[:3],
            field_1[3],
            digitable_line.field_4,
            digitable_line.field_5[:4],
            digitable_line.field_5[4:],
            field_1[4:9] + field_2[:2],
            field_2[2:5],
            field_2[5],
            field_2[6:9],
            field_2[9],
            field_3[:9],
            field_3[9],
        ]

        return BarcodeService().validate("".join(barcode_components))
