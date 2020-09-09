# Author: Reika Kosuda
import sqlalchemy
from db import metadata, engine

timelines = sqlalchemy.Table(
    "timelines",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("event_date", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("place", sqlalchemy.String, default=True),
    sqlalchemy.Column("content", sqlalchemy.String, default=True),
    sqlalchemy.Column("deleted", sqlalchemy.Integer, default=True),
)

metadata.create_all(bind=engine)
