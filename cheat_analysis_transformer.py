from sentence_transformers import SentenceTransformer, util

# مدل چندزبانه که برای زبان فارسی نیز مناسب است
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def is_valid_answer(answer):
    """بررسی اعتبار پاسخ"""
    return (
        answer.get("text") not in [None, "", " "] and 
        isinstance(answer.get("time_taken"), (int, float)) and 
        answer.get("time_taken") > 0
    )

def analyze_similarities(student_data, similarity_threshold=0.3):
    results = []
    for i in range(len(student_data)):
        s1 = student_data[i]
        for j in range(i + 1, len(student_data)):
            s2 = student_data[j]

            for a1 in s1["answers"]:
                for a2 in s2["answers"]:
                    if (
                        a1["question_id"] == a2["question_id"]
                        and is_valid_answer(a1)
                        and is_valid_answer(a2)
                    ):
                        embedding1 = model.encode(a1["text"], convert_to_tensor=True)
                        embedding2 = model.encode(a2["text"], convert_to_tensor=True)
                        similarity = util.pytorch_cos_sim(embedding1, embedding2).item()

                        print(f"📊 شباهت معنایی ({a1['question_id']}): {similarity:.2f}")
                        print(a1)
                        print(a2)

                        if similarity >= similarity_threshold:
                            results.append({
                                "student1": s1["student_id"],
                                "student2": s2["student_id"],
                                "question_id": a1["question_id"],
                                "similarity": round(similarity * 100, 2)
                            })
    return results

def analyze_time(student_data, time_threshold=15):
    results = []
    for i in range(len(student_data)):
        s1 = student_data[i]
        for j in range(i + 1, len(student_data)):
            s2 = student_data[j]

            for a1 in s1["answers"]:
                for a2 in s2["answers"]:
                    if (
                        a1["question_id"] == a2["question_id"]
                        and is_valid_answer(a1)
                        and is_valid_answer(a2)
                    ):
                        time_diff = abs(a1["time_taken"] - a2["time_taken"])
                        if time_diff <= time_threshold:
                            results.append({
                                "student1": s1["student_id"],
                                "student2": s2["student_id"],
                                "question_id": a1["question_id"],
                                "time_difference": time_diff
                            })
    return results
