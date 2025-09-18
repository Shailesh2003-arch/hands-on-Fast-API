from fastapi import FastAPI
import schemas
import models
from database import engine
app = FastAPI()


models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(blog:schemas.Blog):
    return {
        'data':blog
    }