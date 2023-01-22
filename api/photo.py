from fastapi.routing import APIRouter
from models import Photo
from typing import List

router = APIRouter(
    prefix="/photos"
)


@router.get(
    "/all",
    response_model=List[Photo]
)
async def get_all_photos():
    photos = await Photo.objects.all()
    return photos

@router.post(
    "/",
    response_model=Photo,
    response_model_exclude={"galleryitems"}
)
async def create_photo(photo: Photo):
    return await photo.save()

