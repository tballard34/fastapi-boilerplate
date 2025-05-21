from pydantic import BaseModel


class Example(BaseModel):
    speaker: str
    start_time: float
    end_time: float
    text: str
