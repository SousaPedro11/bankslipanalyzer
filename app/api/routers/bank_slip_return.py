from fastapi import APIRouter, File, UploadFile

from app.api.helpers.validators import validate_file_extension

router = APIRouter()


@router.post("/return")
async def validate_return():
    return "Is valid"


@router.post("/return/file")
async def validate_return_file(
    file: UploadFile = File(description="RET file to be validated"),
):

    validate_file_extension(file.filename, ".RET")

    return "Is valid"
