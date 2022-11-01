from data import question_data, new_set
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in new_set:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_more_questions():
    quiz.next_question()

print(f"You have completed the quiz with the final score of {quiz.score}/{quiz.question_number}.")