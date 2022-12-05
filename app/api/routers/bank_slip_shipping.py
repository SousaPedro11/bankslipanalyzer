from fastapi import APIRouter, File, UploadFile

from app.api.helpers.validators import validate_file_extension

router = APIRouter()


@router.post("/shipping")
async def validate_shipping():
    return "Is valid"


@router.post("/shipping/file")
async def validate_shipping_file(
    file: UploadFile = File(description="REM file to be validated"),
):
    validate_file_extension(file.filename, ".REM")

    return "Is valid"
