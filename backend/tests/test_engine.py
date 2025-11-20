from sqlalchemy import inspect, text
from backend.app.database.database_engine import engine, init_db
from app.models.tickers import Tickers


def test_engine_alive():
    with engine.connect() as conn:
        result = conn.scalar(text("SELECT 1"))
        assert result == 1
    print("✅ SELECT 1 прошёл")


def test_create_tables():
    """2. Создаём таблицы и проверяем, что они появились."""
    init_db()
    insp = inspect(engine)
    assert "tickers" in insp.get_table_names()
    print("✅ Таблица tickers создана")


if __name__ == "__main__":
    test_engine_alive()
    test_create_tables()
    print("🎉 Всё работает!")
