from sqlalchemy import Column, Integer, String
from ..database.database import Base


class Tickers(Base):
    __tablename__ = "tickers"
    id = Column(Integer, primary_key=True)
    ticker_name = Column(String(50), nullable=False)
