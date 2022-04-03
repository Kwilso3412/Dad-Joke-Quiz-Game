#This class is used to create the quiz object and corresponding methods

class Quiz_game:
    def __init__(self, question_list):
        self.question_number = 0
        #used for getting the score
        self.score = 0
        #This will be used to hold the question bank
        self.question_list = question_list

#method used for getting the current  question
    def next_question (self,questions):
        self.question_number += 1
        current_question = question.question_list
        for question in questions:
            user_answer = input(f"{self.question_number: {current_question.question_list}}")
        self.check_answer(user_answer, current_question.answer)


#used for checking the answer and if correct it gives a score
    def check_answer(self, user_answer, answer):
        point = 0
        if user_answer ==  answer:
            point += 1
        else:
            point += 0

    def remaining_questions(self):
            return self.question_number < len(self.question_list)

#question class is used for creating question object and corresponding methods
class Question:
    def __init__(self, question_list, answer):
        self.question_list = question_list
        self.answer = answer