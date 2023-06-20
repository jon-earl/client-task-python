from src.user.answers import Answers


class User:
    def __init__(self, id):
        self.id = id
        self.answers = []

    def get_answers(self, survey_id):
        return next(
            (answer for answer in self.answers if answer.survey_id == survey_id), [])

    def set_answers(self, survey_id, answers):
        self.answers.append(Answers(survey_id, answers))
