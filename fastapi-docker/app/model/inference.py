from pathlib import Path
import json

import tensorflow as tf
import numpy as np

import utils
import models

BASE_DIR = Path(__file__).resolve(strict=True).parent
WEIGHTS_PATH = 'saved_weights.h5'
REFERENCE_PATH = 'reference_data.json'
INPUT_SHAPE = (200,2)
PARAMS = {
    'hidden_size':128,
    'batch_size':22,            # fix : must be equaled with number of test pairs 
    'patch_size':10,
    'heads':8,
    'n_layers':12,
    'mlp_units':[256, 128],
    'dropout':0,
    'mlp_dropout':0
}

# get model & weights & reference data
with open('', 'rb') as f:
    ref_dict = json.load(REFERENCE_PATH)
    ViT = models.ViTBaseModel(INPUT_SHAPE, PARAMS)
    model = models.binary_siamese_net(INPUT_SHAPE, base_model= ViT.model())
    model.load_weights(WEIGHTS_PATH)


classes = {
    0: 'numbers 0',
    1: 'numbers 1',
    2: 'numbers 2',
    3: 'numbers 3',
    4: 'numbers 4',
    5: 'numbers 5',
    6: 'numbers 6',
    7: 'numbers 7',
    8: 'numbers 8',
    9: 'numbers 9',
    10: 'katakana 1',
    11: 'katakana 2',
    12: 'katakana 3',
    13: 'katakana 4',
    14: 'katakana 5',
    15: 'katakana 6',
    16: 'katakana 7',
    17: 'katakana 8',
    18: 'katakana 9',
    19: 'katakana 10',
    20: 'katakana 11',
    21: 'katakana 12',
}

def prediction(data):
    eval_batch, eval_target = utils.get_eval_batch(data, ref_dict)

    probs = model.predict_on_batch(eval_batch)
    predict_class = np.argmax(probs)
    answer_class = np.argmax(eval_target)

    return classes[predict_class], classes[answer_class]