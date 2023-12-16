student_heights = input("Input the list of students' heights separated by blank space ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

print(f"The average height of the students is {(total_height // len(student_heights))}")

# print(f"The average height of the students is {}")