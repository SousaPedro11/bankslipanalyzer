from fastapi import APIRouter, Depends, File, UploadFile

from app.api.helpers.validators import validate_lpn_file
from app.api.schemas.nexxera_document import ShippingFileSchema, ShippingInputSchema
from bank_shipping.app.services.shipping import BankSlipShippingService

router = APIRouter()


def get_bank_slip_shipping_service() -> BankSlipShippingService:
    return BankSlipShippingService()


# @router.post("/shipping/lpn", response_model=ShippingFileSchema)
@router.post("/shipping/lpn")
async def validate_shipping(
    shipping: ShippingInputSchema,
    service: BankSlipShippingService = Depends(get_bank_slip_shipping_service),
) -> str:
    service.get_bank_slip_shipping_return(shipping.content)
    return "In development"


@router.post("/shipping/lpn/file", response_model=ShippingFileSchema)
async def validate_shipping_file(
    file: UploadFile = File(description="LPN .REM file to be validated"),
    service: BankSlipShippingService = Depends(get_bank_slip_shipping_service),
) -> ShippingFileSchema:
    validate_lpn_file(str(file.filename))

    shipping_content = await file.read()
    bank_slip_shipping = service.get_bank_slip_shipping_return(shipping_content.decode("utf-8"))

    return bank_slip_shipping
