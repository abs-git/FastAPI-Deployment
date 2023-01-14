from fastapi import FastAPI
from pydantic import BaseModel
from app.model import inference

app = FastAPI()

class Input(BaseModel):
    eye_writing_character: dict

class Output(BaseModel):
    cls: str


@app.get("/")
def home():
    return {"title": "Hello Coder follower :)"}

@app.get('/upload')
def upload():
    return {'disc': 'upload a data'}

@app.post('/predict', response_model=Output)
def predict(data: Input):
    cls = inference.prediction(data)

    # 이미지 출력


    return {'character': cls}