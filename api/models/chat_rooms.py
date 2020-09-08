# Author:  Reika Kosuda
import sqlalchemy
from db import metadata, engine

chat_rooms = sqlalchemy.Table(
    "chat_rooms",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("deleted", sqlalchemy.Integer, default=True),
)
