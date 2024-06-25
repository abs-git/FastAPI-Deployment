import shutil
import os
import json

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .schemas import AwesomForm
from .model import inference

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/root/', response_class=HTMLResponse)
def root(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('home.html', context)

@app.get('/root/{user_name}', response_class=HTMLResponse)
def write_root(request: Request, user_name: str):
    context = {'request': request,
               'username': user_name}
    return templates.TemplateResponse('home.html', context)


UPLOAD_FILES_DIR = './uploaded_files/'

@app.get('/awesome', response_class=HTMLResponse)
def get_form(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('awesome.html', context) 

@app.post('/awesome', response_class=HTMLResponse)
def post_form(request: Request, info: AwesomForm = Depends(AwesomForm.as_form)):

    # file upload and save
    with open(UPLOAD_FILES_DIR + f'{info.file.filename}', 'wb') as buffer:
        shutil.copyfileobj(info.file.file, buffer)

    # load the saved file
    file_path = os.path.join(UPLOAD_FILES_DIR, f'{info.file.filename}')
    with open(file_path, 'r') as f:
        data = json.load(f)

    # predict the class and save the plot images
    results = inference.prediction(data)

    context = {'request': request,
               'info': info,
               'answer': results[0],
               'predict': results[1],
               'ref_img': results[2],
               'real_img': results[3]
    }
    return templates.TemplateResponse('predict.html', context)
