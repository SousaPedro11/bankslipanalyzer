from fastapi import APIRouter

from app.api.routers import bank_slip, bank_slip_return, bank_slip_shipping

api_router = APIRouter()

api_router.include_router(
    router=bank_slip.router,
    tags=["Bank Slip"],
)

api_router.include_router(
    router=bank_slip_return.router,
    tags=["Bank Slip Return"],
)

api_router.include_router(
    router=bank_slip_shipping.router,
    tags=["Bank Slip Shipping"],
)
