import shutil
import os
import json

import time

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas import AwesomeForm
from app.model import inference

app = FastAPI()

ROOT = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(directory=os.path.join(ROOT, 'templates'))

@app.get('/root/{user_name}', response_class=HTMLResponse)
def root_get(request: Request, user_name: str):
    context = {'request': request,
               'username': user_name, 
               'date': time.time()}
    return templates.TemplateResponse('home.html', context)

@app.post('/root/', response_class=HTMLResponse)
def root_post(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('home.html', context)

UPLOAD_FILES_DIR = './uploaded_files/'

@app.get('/awesome', response_class=HTMLResponse)
def get_form(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('awesome.html', context) 

@app.post('/awesome', response_class=HTMLResponse)
def post_form(request: Request, info: AwesomeForm = Depends(AwesomeForm.as_form)):
    
    print(info)

    context = {'request': request,
               'info': info,
               'answer': results[0],
               'predict': results[1],
               'ref_img': results[2],
               'real_img': results[3]
    }
    return templates.TemplateResponse('predict.html', context)
