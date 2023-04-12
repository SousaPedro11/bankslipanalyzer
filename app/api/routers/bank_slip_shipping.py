from fastapi import APIRouter, Depends, File, UploadFile

from app.api.helpers.validators import validate_lpn_file
from app.services.shipping import BankSlipShippingService

router = APIRouter()


def get_bank_slip_shipping_service():
    return BankSlipShippingService()


# @router.post("/shipping", response_model=ShippingFileSchema)
# async def validate_shipping(shipping: ShippingInputSchema, service=Depends(get_bank_slip_shipping_service)):
#     bank_slip_shipping = service.get_bank_slip_shipping(shipping.content)
#     return [bank_slip_shipping]


@router.post("/shipping/file")
async def validate_shipping_file(
    file: UploadFile = File(description="LPN .REM file to be validated"),
    service=Depends(get_bank_slip_shipping_service),
):
    validate_lpn_file(file.filename)

    content = await file.read()
    bank_slip_shipping = service.get_bank_slip_shipping(content.decode("utf-8"))

    return bank_slip_shipping
