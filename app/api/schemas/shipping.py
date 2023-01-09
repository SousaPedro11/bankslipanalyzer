from typing import List, Optional, Text

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


class LotTrailerSchema(FileLineSchema):
    pass


class NexxeraShippingSchema(BaseModel):
    segment_p: SegmentPSchema
    segment_q: SegmentQSchema
    segment_r: Optional[SegmentRSchema]
    segment_s: Optional[SegmentSSchema]
    segment_y: Optional[SegmentYSchema]
    segment_v: Optional[SegmentVSchema]


class ShippingFileSchema(BaseModel):
    header_file: FileHeaderSchema
    header_lot: LotHeaderSchema
    shippings: List[NexxeraShippingSchema]
    trailer_lot: LotTrailerSchema
    trailer_file: FileTrailerSchema
