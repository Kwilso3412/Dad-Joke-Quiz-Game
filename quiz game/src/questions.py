from importlib.util import set_loader


class question:
    def __init__(question_object, question, multiple_choice,  answer, hint):
        question_object.question = question
        question_object.multiple_choice = multiple_choice
        question_object.answer = answer
        question_object.hint = hint
