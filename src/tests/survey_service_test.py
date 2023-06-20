from unittest import TestCase
import pytest
from src.survey.survey_not_found_error import SurveyNotFoundError
from src.survey.survey_service import SurveyService


class SurveyServiceTests(TestCase):

    def setUp(self):
        self.survey_service = SurveyService()

    def test_create_survey(self):
        questions = ['q1']
        id = self.survey_service.create_survey(questions)
        assert id == 0

    def test_get_no_survey(self):
        id = 0
        with pytest.raises(SurveyNotFoundError):
            self.survey_service.get_survey(id)

    def test_get_first_survey(self):
        id = self.survey_service.create_survey(["q1"])
        survey = self.survey_service.get_survey(id)
        assert survey.questions == ["q1"]

    def test_get_many_survey(self):
        self.survey_service.create_survey(["s1q1"])
        id = self.survey_service.create_survey(["s2q1"])
        survey = self.survey_service.get_survey(id)
        assert survey.questions == ["s2q1"]

    def test_edit_survey(self):
        questions = ['q1v1']
        id = self.survey_service.create_survey(questions)
        questions = ['q1v2']
        self.survey_service.update_survey(id, questions)
        survey = self.survey_service.get_survey(id)
        assert survey.questions == ["q1v2"]
