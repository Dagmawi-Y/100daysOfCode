student_scores = input("Enter the scores for students separated by a blank space ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max = 0

for i in student_scores:
    if (i > max):
        max = i

print(max)