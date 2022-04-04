#This class is used to create the quiz object and corresponding methods
from question_bank_data import question_bank

class Quiz_game:
    def __init__(self, question_list):
        self.question_number = 0
        #used for getting the score
        self.score = 0
        #This will be used to hold the question bank
        self.question_list = question_list

#this method wil loop through the questions and then print out the question
    def load_questions(self, questions):
        self.question_number += 1
        for question in questions:
            current_question = question.question_bank
            answer = input(current_question)
            self.check_answer(current_question, answer)

#used for checking the answer and if correct it gives a score
    def check_answer(self, current_question, answer):
        point = 0
        if current_question ==  answer:
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