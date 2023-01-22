import ormar
from .photo import Photo
from .gallery import Gallery
from db import BaseMeta


class GalleryItem(ormar.Model):
    class Meta(BaseMeta):
        tablename = "gallery_items"

    id: int = ormar.Integer(
        primary_key=True,
        autoincrement=True
    )
    photo: Photo = ormar.ForeignKey(
        to=Photo
    )

    gallery: Gallery = ormar.ForeignKey(
        to=Gallery
    )
