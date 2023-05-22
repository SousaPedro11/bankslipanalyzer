import re
from typing import Dict, Optional, Union

from pydantic import BaseModel, Field, root_validator, validator

from app.api.helpers.validators import regex_barcode, regex_digitable_line


class BarcodeInputSchema(BaseModel):
    barcode: str

    @validator("barcode")
    def validate_barcode(cls, value: str) -> str:
        regex = re.compile(regex_barcode())
        if not regex.match(value):
            msg = "Must be 44 only numbers"
            raise ValueError(msg)

        return value


class DigitableLineInputSchema(BaseModel):
    digitable_line: Union[str, Dict[str, str]]

    @validator("digitable_line")
    def validate_digitable_line(cls, value: str) -> str:
        regex = re.compile(regex_digitable_line())

        if not regex.match(value):
            msg = "Must be 47 only numbers or in the format 00000.00000 00000.000000 00000.000000 0 00000000000000"
            raise ValueError(
                msg,
            )

        return value


class BarcodeSchema(BaseModel):
    bank: str = Field(
        ...,
        description="Bank identifier",
        example="104",
        min_length=3,
        max_length=3,
    )
    currency_code: str = Field(
        ...,
        description="Currency code - 9 for Real",
        example="9",
        min_length=1,
        max_length=1,
    )
    vd_general: Optional[str] = Field(
        description="Barcode general verification digit",
        example="1",
        min_length=1,
        max_length=1,
    )
    due_date_factor: str = Field(
        ...,
        description="Due date factor",
        example="0000",
        min_length=4,
        max_length=4,
    )
    document_value: str = Field(
        ...,
        description="Nominal document value",
        example="0000000000",
        min_length=10,
        max_length=10,
    )
    beneficiary_code: str = Field(
        ...,
        description="Beneficiary code",
        example="0000000",
        min_length=7,
        max_length=7,
    )
    sequence_1: str = Field(
        ...,
        description="Our number - Sequence 1",
        example="000",
        min_length=3,
        max_length=3,
    )
    constant_1: str = Field(
        ...,
        description="Constant 1",
        example="0",
        min_length=1,
        max_length=1,
    )
    sequence_2: str = Field(
        ...,
        description="Our number - Sequence 2",
        example="000",
        min_length=3,
        max_length=3,
    )
    constant_2: str = Field(
        ...,
        description="Constant 2",
        example="0",
        min_length=1,
        max_length=1,
    )
    sequence_3: str = Field(
        ...,
        description="Our number - Sequence 3",
        example="000000000",
        min_length=9,
        max_length=9,
    )
    vd_field_free: Optional[str] = Field(
        ...,
        description="Field free verification digit",
        example="0",
        min_length=1,
        max_length=1,
    )


class DigitableLineSchema(BaseModel):
    field_1: str = Field(
        ...,
        description="Field 1 - Positions 1 to 3, 4, 20 to 24 from barcode and verification digit from field 1",
        example="00000.00000",
        min_length=10,
        max_length=11,
    )
    field_2: str = Field(
        ...,
        description="Field 2 - Positions 25 to 34 from barcode and verification digit from field 2",
        example="00000.000000",
        min_length=11,
        max_length=12,
    )
    field_3: str = Field(
        ...,
        description="Field 3 - Positions 35 to 44 from barcode and verification digit from field 3",
        example="00000.000000",
        min_length=11,
        max_length=12,
    )
    field_4: str = Field(
        ...,
        description="Field 4 - Verification digit from barcode (position 5)",
        example="0",
        min_length=1,
        max_length=1,
    )
    field_5: str = Field(
        ...,
        description="Field 5 - Positions 6 to 9 (due date factor) and positions 10 to 19 (document value) from barcode",
        example="00000000000000",
        min_length=14,
        max_length=14,
    )

    @validator("field_1", "field_2", "field_3")
    def validate_field(cls, value: str) -> str:
        if "." not in value:
            value = f"{value[:5]}.{value[5:]}"
        return value


class BarcodeOutputSchema(BarcodeSchema):
    due_date: Optional[str] = Field(
        description="Calculated due date",
        example="01/01/2021",
        default=None,
    )

    expected_barcode: Optional[BarcodeSchema] = Field(
        description="Expected barcode",
        default=None,
    )

    expected_digitable_line: Optional[DigitableLineSchema] = Field(
        description="Expected digitable line",
        default=None,
    )
    status: Optional[str] = Field(
        description="Status",
        example="valid",
        default=None,
    )

    @root_validator
    def validate_barcode(cls, values):
        barcode_expected = values.get("expected_barcode", None)
        if not (barcode_expected and values | barcode_expected.dict() == values):
            values["status"] = "barcode is invalid"
        else:
            values["status"] = "valid"

        return values


class DigitableLineOutputSchema(DigitableLineSchema):
    barcode: Optional[BarcodeOutputSchema] = Field(
        description="Barcode",
        default=None,
    )
    status: Optional[str] = Field(
        description="Status",
        example="valid",
        default=None,
    )

    @root_validator
    def validate_digitable_line(cls, values):
        barcode_expected = values.get("barcode", None)
        if not (barcode_expected and values | barcode_expected.expected_digitable_line.dict() == values):
            values["status"] = "digitable line is invalid"
        else:
            values["status"] = "valid"

        return values
