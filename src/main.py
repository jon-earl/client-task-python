# main.py
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.survey.survey_not_found_error import SurveyNotFoundError
from src.survey.survey_service import SurveyService

from src.user.user_service import UserService

app = FastAPI()


class Survey(BaseModel):
    id: int
    questions: List[str]


class SurveyRequest(BaseModel):
    questions: List[str]


class SurveyCreateResponse(BaseModel):
    id: int


survey_service = SurveyService()


@app.post("/surveys/")
async def create_survey(survey: SurveyRequest):
    survey_id = survey_service.create_survey(survey.questions)
    return SurveyCreateResponse(id=survey_id)


@app.get("/surveys/{survey_id}", response_model=Survey)
async def get_survey(survey_id: int):
    try:
        survey = survey_service.get_survey(survey_id)
    except SurveyNotFoundError:
        raise HTTPException(status_code=404, detail="Survey not found")
    return Survey(id=survey.id, questions=survey.questions)


@app.post("/surveys/{survey_id}", response_model=Survey)
async def update_survey(survey_id: int, surveyRequest: SurveyRequest):
    try:
        survey = survey_service.update_survey(
            survey_id, surveyRequest.questions)
        print(survey)
    except SurveyNotFoundError:
        raise HTTPException(status_code=404, detail="Survey not found")
    return Survey(id=survey.id, questions=survey.questions)
