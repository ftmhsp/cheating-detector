from fastapi import FastAPI
from schemas import StudentResponse
from database import save_student_response, fetch_all_responses
from cheat_analysis_transformer import analyze_similarities, analyze_time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit")
def submit_response(student: StudentResponse):
    save_student_response(student)
    return {"message": "Student response saved successfully", "student_id": student.student_id}

@app.get("/analyze")
def analyze_cheating():
    student_data = fetch_all_responses()
    print("🔍 داده‌های واکشی‌شده:", student_data)
    text_matches = analyze_similarities(student_data, similarity_threshold=0.3)
    print("Text similarity matches:", text_matches)
    time_matches = analyze_time(student_data, time_threshold=15)
    print("Time similarity matches:", time_matches)

    return {
        "text_similarity_suspects": text_matches,
        "time_similarity_suspects": time_matches
    }

