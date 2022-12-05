from fastapi import APIRouter, Depends

from app.api.schemas.bank_slip import (
    BarcodeInputSchema,
    BarcodeOutputSchema,
    DigitableLineInputSchema,
    DigitableLineOutputSchema,
)
from app.services.barcode import BarcodeService
from app.services.digitable_line import DigitableLineService

router = APIRouter()


def get_barcode_service():
    return BarcodeService()


def get_digitable_line_service():
    return DigitableLineService()


@router.post("/digitable-line", response_model=DigitableLineOutputSchema)
async def validate_by_digitable_line(
    digitable_line: DigitableLineInputSchema,
    service: DigitableLineService = Depends(get_digitable_line_service),
):
    result = service.validate(digitable_line.digitable_line)

    return result


@router.post("/barcode", response_model=BarcodeOutputSchema)
async def validate_by_barcode(
    barcode: BarcodeInputSchema,
    service=Depends(get_barcode_service),
):

    result = service.validate(barcode.barcode)

    return result
