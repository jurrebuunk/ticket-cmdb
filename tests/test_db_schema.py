from sqlalchemy import create_engine, inspect

from app.models import Base


def test_tables_exist():
    """Create the metadata in an in-memory SQLite DB and assert tables exist."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    inspector = inspect(engine)
    tables = set(inspector.get_table_names())

    assert {"assets", "tickets", "comments"}.issubset(tables)
