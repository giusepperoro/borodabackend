from fastapi.routing import APIRouter
import api.photo as photo

router = APIRouter(
    prefix="/api"
)
router.include_router(
    photo.router
)
