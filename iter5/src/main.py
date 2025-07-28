from fastapi import FastAPI
from models import MoveFile
from organizer import FileOrganizer,Logger




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
