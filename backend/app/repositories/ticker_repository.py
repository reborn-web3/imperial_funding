from typing import List
from sqlalchemy.orm import Session
from ..models.tickers import Tickers


class TickerRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> List[Tickers]:
        return self.db.query(Tickers).all()

    def get_by_exchange(self): ...

    def get_by_ticker(self): ...
