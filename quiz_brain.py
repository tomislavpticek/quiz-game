class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_more_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        answer = input(f"Q {self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        return self.check_answer(answer, self.question_list[self.question_number].answer)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print(f"Correct :).")
        else:
            print(f"Incorrect :(, the correct answer was {correct_answer}")

        self.question_number += 1
        print(f"Your current score is {self.score}/{self.question_number}\n")