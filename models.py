from pydantic import BaseModel,Field
from typing import Optional


class MoveFile(BaseModel):
    source:Optional[str]=""
    category:Optional[str]=""
