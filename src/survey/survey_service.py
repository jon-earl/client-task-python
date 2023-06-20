import inspect
from src.survey.survey import Survey
from src.survey.survey_not_found_error import SurveyNotFoundError


class SurveyService:

    def __init__(self):
        self.latest_id = 0
        self.surveys = []

    def create_survey(self, questions):
        survey = Survey(self.latest_id, questions)
        self.surveys.append(survey)
        self.latest_id += 1
        return survey.id

    def get_survey(self, id):
        print("GET SURVEY LIST")
        for survey in self.surveys:
            print(str(survey.id) + " " + str(survey.questions))
        survey = next(
            (survey for survey in self.surveys if survey.id == id), None)
        if (survey == None):
            raise SurveyNotFoundError
        return survey

    def update_survey(self, id, questions):
        survey = self.get_survey(id)
        survey.questions = questions
        return survey
