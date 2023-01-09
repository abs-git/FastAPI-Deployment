import pickle
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open('', 'rb') as f:
    model = pickle.load(f)

classes = {

}

def prediction(data):
    data 

    probs = model.predict()
    return classes[probs]