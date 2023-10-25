from fastapi import FastAPI, HTTPException

from .service import get_time

app = FastAPI()


@app.get("/todate/{prompt}")
def index(prompt: str):
    try:
        return {"msg": get_time(prompt)}
    except ValueError:
        raise HTTPException(status_code=403, detail="Invalid prompt")
