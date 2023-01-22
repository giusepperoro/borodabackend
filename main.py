from fastapi import FastAPI
import uvicorn
from api import router


app = FastAPI(
    title="Best Practice CHIN CHIN"
)
app.include_router(
    router
)

if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=3000
    )


