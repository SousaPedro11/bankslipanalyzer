from fastapi import APIRouter

from bank_shipping.app.api.routers.bank_slip_shipping import router

shipping_router = APIRouter()

shipping_router.include_router(
    router=router,
    tags=["Bank Slip Shipping (LPN)"],
)
