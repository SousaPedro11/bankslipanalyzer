from fastapi import APIRouter, Depends, File, UploadFile

from app.api.helpers.validators import validate_file_extension
from app.api.schemas.nexxera_document import ReturnFileSchema
from bank_return.app.services.bank_return import BankSlipReturnNexxeraService

router = APIRouter()


def get_bank_slip_return_service():
    return BankSlipReturnNexxeraService()


@router.post("/return/cob")
async def validate_return():
    return "In development"


@router.post("/return/cob/file", response_model=ReturnFileSchema)
async def validate_return_file(
    file: UploadFile = File(description="RET file to be validated"),
    service=Depends(get_bank_slip_return_service),
):
    validate_file_extension(file.filename, ".RET")

    return_content = await file.read()

    bank_slip_return = service.get_bank_slip_shipping_return(return_content.decode("utf-8"))
    return bank_slip_return
