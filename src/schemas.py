from pydantic import BaseModel


class Offer(BaseModel):
    sdp: str
    type: str
    exercise: str
    cnt: str
    set: str
    breaktime: str

class Info(BaseModel):
<<<<<<< HEAD
    exercise: str
    cnt: str
    set: str
    breaktime: str
=======
    exercise: list
    cnt: list
    set: list
    exit: int

>>>>>>> f538419857fde15e7b275b8ec49b380a54fe6f3d
class Live(BaseModel):
    sdp: str
    type: str
