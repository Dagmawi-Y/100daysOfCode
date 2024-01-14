import random

''' List Comprehension '''
#
# new_list = [n + 1 for n in [1, 2, 3]]
#
# name_in_list = [n for n in "Dagmawi"]
#
# range_in_list = [n * 2 for n in range(0, 10)]
#
# print(range_in_list)
# print(name_in_list)
# print(new_list)


''' Dictionary Comprehension '''
#
# student_scores = {
#     "alex": 89,
#     "diriba": 90,
#     "daggy": 99
# }

name = ["Dag", "Mel", "Mus", "Mer"]
new_scores = {student: random.randint(1, 100) for student in name}
print(new_scores)

passed_students = {passed_student: score for (passed_student, score) in new_scores.items() if score > 50}
print(passed_students)
