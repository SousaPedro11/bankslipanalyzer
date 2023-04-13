from fastapi import APIRouter, Depends, File, UploadFile

from app.api.helpers.validators import validate_lpn_file
from app.api.schemas.nexxera_document import ShippingInputSchema
from bank_shipping.app.services.shipping import BankSlipShippingService

router = APIRouter()


def get_bank_slip_shipping_service():
    return BankSlipShippingService()


# @router.post("/shipping/lpn", response_model=ShippingFileSchema)
@router.post("/shipping/lpn")
async def validate_shipping(shipping: ShippingInputSchema, service=Depends(get_bank_slip_shipping_service)):
    service.get_bank_slip_shipping_return(shipping.content)
    return "In development"


@router.post("/shipping/lpn/file")
async def validate_shipping_file(
    file: UploadFile = File(description="LPN .REM file to be validated"),
    service=Depends(get_bank_slip_shipping_service),
):
    validate_lpn_file(file.filename)

    shipping_content = await file.read()
    bank_slip_shipping = service.get_bank_slip_shipping_return(shipping_content.decode("utf-8"))

    return bank_slip_shipping
