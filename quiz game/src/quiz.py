from importlib.util import set_loader

#question class is used for creating question object and corresponding methods
class question:
    def __init__(question_object, question, multiple_choice,  answer, hint):
        question_object.question = question
        question_object.multiple_choice = multiple_choice
        question_object.answer = answer
        question_object.hint = hint


#This class is used to create the quiz object and corresponding methods
class quiz:
    def __init__(quiz_object, question_list):
        quiz_object.question_number = 0
        quiz_object.score = 0
        quiz_object.question_list = question_list

    def next_question (self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer =input(f"{self.question_number: {current_question.question}}" + "\n" + "{current_question.multiple_choice}")
        
