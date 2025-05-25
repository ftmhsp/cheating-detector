import os
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from schemas import StudentResponse

base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, "responses.db")
print("📁 مسیر responses.db:", db_path)

engine = create_engine(f"sqlite:///{db_path}", echo=False)
metadata = MetaData()

answers_table = Table(
    "answers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", String),
    Column("question_id", String),
    Column("text", String),
    Column("time_taken", Integer)
)

metadata.create_all(engine)

def save_student_response(student: StudentResponse):
    with engine.begin() as conn:
        for answer in student.answers:
            conn.execute(answers_table.insert().values(
                student_id=student.student_id,
                question_id=answer.question_id,
                text=answer.text,
                time_taken=answer.time_taken
            ))

def fetch_all_responses():
    with engine.connect() as conn:
        rows = conn.execute(answers_table.select()).fetchall()

    students = {}
    for row in rows:
        student_id = row[1]
        if student_id not in students:
            students[student_id] = []
        students[student_id].append({
            "question_id": row[2],
            "text": row[3],
            "time_taken": row[4]
        })

    return [{"student_id": sid, "answers": answers} for sid, answers in students.items()]