from fastapi import FastAPI

# routers
from app.sentiments.router import router as sentiment_router
from app.summaries.router import router as summaries_router
from app.users.router import router as users_router

app = FastAPI()


@app.get('/', tags=['Home'])
def index():
    return {'message': 'Welcome!'}


app.include_router(sentiment_router)
app.include_router(summaries_router)
app.include_router(users_router)
