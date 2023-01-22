from fastapi import HTTPException,status
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


@router.get(
    "/{photo_id}",
    response_model=Photo,
    response_model_exclude={"galleryitems"}
)
async def get_photo_by_id(photo_id: int):
    photo = await Photo.objects.get_or_none(
        pk=photo_id
    )
    if not photo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Фото с id {photo_id} не найдено"
        )
    return photo
