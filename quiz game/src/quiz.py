
#This class is used to create the quiz object and corresponding methods
class Quiz_game:
    def __init__(quiz_object, question_list):
        quiz_object.question_number = 0
        quiz_object.score = 0

        #This will be used to hold the question bank
        quiz_object.question_list = question_list

    def next_question (self):
        #shows the current question
        current_question = self.question_list[self.question_number]
        #adds one to cycle to the next question
        self.question_number += 1
        #gets the users response for the next question 
        user_answer = input(f"{self.question_number: {current_question.question}}" + "\n" + "{current_question.multiple_choice}")
        #checks if the question is correct 
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        user_answer = user_answer.lower()
        answer = answer.lower()
        if user_answer == answer:
            self.score += 1
            print("Thats correct!")
        else:
            print("oops that is not the correct answer" + "\n" + f"The correct answer was: {answer}")
        print(f"Your current score is : {self.score}"/{self.question_number})
    def remaining_questions(self):
            return self.question_number < len(self.question_list)

#question class is used for creating question object and corresponding methods
class Question:
    def __init__(question_object, question, multiple_choice,  answer, hint):
        question_object.question = question
        question_object.multiple_choice = multiple_choice
        question_object.answer = answer
        question_object.hint = hint