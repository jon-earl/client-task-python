import unittest
from fastapi.testclient import TestClient
import pytest

from src.main import app

client = TestClient(app)


class ApiTest(unittest.TestCase):
    @pytest.mark.order(1)
    def test_new_survey(self):
        response = client.post(
            "/surveys/",
            headers={},
            json={"questions": ["q1", "q2", "q3"]},
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": 0,
        }

    @pytest.mark.order(2)
    def test_get_survey(self):
        response = client.get(
            "/surveys/0"
        )
        assert response.status_code == 200
        assert response.json() == {'id': 0, 'questions': ['q1', 'q2', 'q3']}

    @pytest.mark.order(3)
    def test_get_survey_not_found(self):
        response = client.get(
            "/surveys/6"
        )
        assert response.status_code == 404

    @pytest.mark.order(4)
    def test_edit_survey(self):
        response = client.post(
            "/surveys/0",
            headers={},
            json={"questions": ["q1v2", "q2v2", "q3v2"]},
        )
        assert response.status_code == 200

        response = client.get(
            "/surveys/0"
        )
        assert response.status_code == 200
        assert response.json() == {'id': 0, 'questions': [
            'q1v2', 'q2v2', 'q3v2']}
