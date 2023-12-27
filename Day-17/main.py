# class User:
#     def __init__(self, username):
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def print_user_name(self):
#         print(self.username)
#
#     def follow_user(self, user):
#         self.following += 1
#         user.followers += 1
#
#
# user_1 = User(username="dag")
#
# user_2 = User(username="yoh")
#
# user_1.follow_user(user_2)
#
#

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score is {quiz.score}/{quiz.question_number}")
