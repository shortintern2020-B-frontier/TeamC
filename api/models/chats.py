import sqlalchemy
from db import metadata, engine

chats = sqlalchemy.Table(
    "chats",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("chat_room_id", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("deleted", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("content", sqlalchemy.String, default=True),
    sqlalchemy.Column("created_at", sqlalchemy.String, default=True),
)

metadata.create_all(bind=engine)