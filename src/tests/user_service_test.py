from unittest import TestCase
import pytest
from src.user.user import User
from src.user.user_not_found_error import UserNotFoundError
from src.user.user_service import UserService


class UserServiceTest(TestCase):

    def setUp(self):
        self.user_service = UserService()

    def test_new_user(self):
        user = self.user_service.new_user()
        assert type(user) is User

    def test_get_no_user(self):
        id = 0
        with pytest.raises(UserNotFoundError):
            self.user_service.get_user(id)

    def test_get_first_user(self):
        new_user = self.user_service.new_user()
        user = self.user_service.get_user(new_user.id)
        assert type(user) is User

    def test_answer_survey_questions(self):
        new_user = self.user_service.new_user()
        survey_id = 0
        answers = ['a1']
        self.user_service.answer_survey(new_user.id, survey_id, answers)

        user = self.user_service.get_user(new_user.id)
        assert user.get_answers(survey_id).answers == ['a1']
