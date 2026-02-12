from sqlalchemy import create_engine, inspect

from app.models import Base


def test_models_create_tables():
    """Create an in-memory SQLite DB from the models' metadata and assert
    the expected tables and columns exist.
    """
    engine = create_engine("sqlite:///:memory:")

    inspector = inspect(engine)
    # no tables before creating
    assert inspector.get_table_names() == []

    Base.metadata.create_all(engine)

    inspector = inspect(engine)
    tables = set(inspector.get_table_names())
    assert {"assets", "tickets", "comments"}.issubset(tables)

    assets_cols = {c["name"] for c in inspector.get_columns("assets")}
    assert {"id", "name", "type", "created_at", "updated_at"}.issubset(assets_cols)

    tickets_cols = {c["name"] for c in inspector.get_columns("tickets")}
    assert {"id", "title", "description", "status", "asset_id", "created_at"}.issubset(
        tickets_cols
    )

    comments_cols = {c["name"] for c in inspector.get_columns("comments")}
    assert {"id", "ticket_id", "body", "created_at"}.issubset(comments_cols)
