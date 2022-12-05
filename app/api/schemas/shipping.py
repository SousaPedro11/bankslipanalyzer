from pydantic import BaseModel


class BankSlipShippingSchema(BaseModel):
    content: str
