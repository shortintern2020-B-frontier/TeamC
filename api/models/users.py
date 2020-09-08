# Author hirata
import sqlalchemy
from db import metadata, engine

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("username", sqlalchemy.String, index=True),
    sqlalchemy.Column("email", sqlalchemy.String, index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("user_id", sqlalchemy.String, default=True),
    sqlalchemy.Column("status", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("comment", sqlalchemy.String, default=True),
    sqlalchemy.Column("status_update_at", sqlalchemy.String, default=True),
    sqlalchemy.Column("longitude", sqlalchemy.Float, default=True),
    sqlalchemy.Column("latitude", sqlalchemy.Float, default=True),
)

metadata.create_all(bind=engine)