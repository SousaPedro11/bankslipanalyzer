from fastapi import APIRouter, File, UploadFile

from app.api.helpers.validators import validate_file_extension

router = APIRouter()


@router.post("/return/cob")
async def validate_return():
    return "In development"


@router.post("/return/cob/file")
async def validate_return_file(
    file: UploadFile = File(description="RET file to be validated"),
):
    validate_file_extension(file.filename, ".RET")

    return "In development"
