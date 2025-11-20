from app.repositories.ticker_repository import TickerRepository


async def test_get_all():
    db = None
    ticker_repository = TickerRepository(db)
    assert len(ticker_repository.get_all()) == 0
