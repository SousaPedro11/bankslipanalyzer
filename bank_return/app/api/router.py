from fastapi import APIRouter

from bank_return.app.api.routers.bank_slip_return import router

return_router = APIRouter()

return_router.include_router(
    router=router,
    tags=["Bank Slip Return (NEXXERA)"],
)
