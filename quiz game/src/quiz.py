#This class is used to create the quiz object and corresponding methods

#question class is used for creating question object and corresponding methods
class Question:
    def __init__(self, question_list, answer):
        self.question_list = question_list
        self.answer = answer