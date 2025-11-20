from sqlalchemy import Column, Float, Integer, String, DateTime
from ..database.database_engine import Base


class Tickers(Base):
    __tablename__ = "tickers"

    ticker_name = Column(String(50), nullable=False)
    funding_rate = Column(Float, nullable=False)
    funding_time = Column(DateTime, nullable=False)
