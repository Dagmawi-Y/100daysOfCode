student_scores = {
    "Dag" : 90,
    "Ron" : 80,
    "Hermoine": 77,
    "Neville": 75
}

# emp dict student grades
student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 90:
        student_grades[key] = "Outstanding"
    elif score > 75 or score < 90:
        student_grades[key] = "Great"
print(student_grades)