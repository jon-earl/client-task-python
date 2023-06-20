from src.user.user import User
from src.user.user_not_found_error import UserNotFoundError


class UserService:

    def __init__(self):
        self.latest_id = 0
        self.users = []

    def new_user(self):
        user = User(self.latest_id)
        self.users.append(user)
        self.latest_id += 1
        return user

    def get_user(self, id):
        user = next((user for user in self.users if user.id == id), None)
        if (user == None):
            raise UserNotFoundError
        return user

    def answer_survey(self, user_id, survey_id, answers):
        user = self.get_user(user_id)
        user.set_answers(survey_id, answers)
