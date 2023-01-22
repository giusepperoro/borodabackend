import datetime
from db import BaseMeta
import ormar


class Photo(ormar.Model):
    class Meta(BaseMeta):
        tablename = "photos"

    id: int = ormar.Integer(
        primary_key=True,
        autoincrement=True
    )
    path: str = ormar.String(
        max_length=100
    )
    description: str = ormar.String(
        max_length=255
    )
    created: datetime.datetime = ormar.DateTime(
        default=datetime.datetime.now()
    )
