from fastapi import APIRouter

from bank_slip.app.api.routers.bank_slip import router

bank_slip_router = APIRouter()

bank_slip_router.include_router(
    router=router,
    tags=["Bank Slip (CEF)"],
)
