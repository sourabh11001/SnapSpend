from pydantic import BaseModel
from typing import Optional

# This defines what the API expects to receive or return
class ExpenseBase(BaseModel):
    merchant: str
    amount: float
    currency: str = "₹"
    category: str
    date: str

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    ai_raw_summary: Optional[str] = None

    class Config:
        from_attributes = True
