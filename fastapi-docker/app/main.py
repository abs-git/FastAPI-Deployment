from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import prediction


app = FastAPI()

class Input(BaseModel):
    text: str

class Output(BaseModel):
    cls: str


@app.get("/")
def home():
    return {"title": "Hello Coder follower :)"}


@app.post('/predict', response_model=Output)
def predict(data: Input):
    cls = prediction(data)
    return {'character': cls}