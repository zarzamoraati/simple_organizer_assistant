from fastapi import FastAPI
from organizer import FileOrganizer,Logger

from pydantic import BaseModel,Field
from typing import Optional


class MoveFile(BaseModel):
    source:Optional[str]=""
    category:Optional[str]=""



app=FastAPI()

@app.get("/")
def home():
    return {"message":"hello"}

@app.post("/organize")
def operation(payload:MoveFile=None):
    logger=Logger()
    organizer=FileOrganizer(movements=logger)

    if payload:
        payload=payload.model_dump()
        print(payload)

        source=payload["source"]
        category=payload["category"]
        organizer.organize(called_by_user=False,payload=(source,category))
    else:
        organizer.organize()
