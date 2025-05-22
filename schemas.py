from pydantic import BaseModel
from typing import List

class Answer(BaseModel):
    question_id: str
    text: str
    time_taken: int

class StudentResponse(BaseModel):
    student_id: str
    answers: List[Answer]