from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    merchant = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String, default="₹")
    category = Column(String)
    date = Column(String)  # Storing as ISO String (YYYY-MM-DD) for simplicity
    
    # Adding a 'raw_text' column proves you think about debugging AI errors
    ai_raw_summary = Column(String, nullable=True)
