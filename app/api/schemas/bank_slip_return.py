from pydantic import BaseModel


class BankSlipReturnSchema(BaseModel):
    content: str
