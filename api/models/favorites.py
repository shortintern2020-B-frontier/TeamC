import sqlalchemy
from db import metadata, engine

favorites = sqlalchemy.Table(
    "favorites",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("target_user_id", sqlalchemy.Integer, default=True),
)

metadata.create_all(bind=engine)