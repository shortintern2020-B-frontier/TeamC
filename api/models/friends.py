# Author hirata
import sqlalchemy
from db import metadata, engine

friends = sqlalchemy.Table(
    "friends",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_1_id", sqlalchemy.Integer, default=True),
    sqlalchemy.Column("user_2_id", sqlalchemy.Integer, default=True),
)

metadata.create_all(bind=engine)