from datetime import date
from typing import List, Optional

from pydantic import BaseModel

class SaveWorkout(BaseModel):

    workout_session: int
    workout_name : str
    sequence : int
    set : int
    count : int
    breaktime : int


class WorkoutFlow(SaveWorkout):

    id : int
    class Config:
        orm_mode = True


class SaveWorkoutSession(BaseModel):

    date_time : date
<<<<<<< HEAD
=======
    exit: int
>>>>>>> f538419857fde15e7b275b8ec49b380a54fe6f3d

class WorkoutSession(SaveWorkoutSession):

    id: int
   
class Get_WorkoutSession(WorkoutSession):

    class Config:
        orm_mode = True



# class WorkoutDone(BaseModel):

#     id : int
#     workout_flow_id : int
#     done_or_not : bool
