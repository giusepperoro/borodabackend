import ormar
from db import BaseMeta


class Gallery(ormar.Model):
    class Meta(BaseMeta):
        tablename = "galleries"

    id: int = ormar.Integer(
        primary_key=True,
        autoincrement=True
    )
    title: str = ormar.String(
        max_length=100
    )
    description: str = ormar.String(
        max_length=255
    )
