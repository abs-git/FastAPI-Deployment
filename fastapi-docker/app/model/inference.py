import json
import os
import base64

import numpy as np

from ..model import models
from ..model import utils

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
IMAGE_DIR = './templates/img/'
WEIGHTS_PATH = '/saved_weights.h5'
REFERENCE_PATH = '/all_reference.json'
INPUT_SHAPE = (200,2)
PARAMS = {
    'hidden_size':128,
    'batch_size':22,            # fix : must be equaled with number of test pairs 
    'patch_size':10,
    'heads':8,
    'n_layers':8,
    'mlp_units':[64, 32],
    'dropout':0,
    'mlp_dropout':0
}

# load a reference data
with open(DIR_PATH + REFERENCE_PATH) as f:
    ref_dict = json.load(f)

# define model & get weights
ViT = models.ViTBaseModel(INPUT_SHAPE, PARAMS)
classifier = models.binary_siamese_net(INPUT_SHAPE, base_model= ViT.model())
classifier.load_weights(DIR_PATH + WEIGHTS_PATH)
print(classifier.summary())


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
    # create the batch
    eval_batch, eval_target = utils.get_eval_batch(data, ref_dict)

    # predict and return class type
    probs = classifier.predict_on_batch(eval_batch)
    target = np.argmax(eval_target)
    predict = np.argmax(probs)

    answer_class = classes[target]
    predict_class = classes[predict]

    # create the images and save
    ref_key = list(ref_dict.keys())[0]
    real_key = list(data.keys())[0]
    utils.plot_images(data[real_key], IMAGE_DIR+answer_class)
    utils.plot_images(ref_dict[ref_key][str(predict)][0], IMAGE_DIR+predict_class)
    
    # load the saved images
    ref_img_path = IMAGE_DIR+answer_class+'.png'
    with open(ref_img_path, 'rb') as f:
        ref_content = base64.b64encode(f.read())

    real_img_path = IMAGE_DIR+predict_class+'.png'
    with open(real_img_path, 'rb') as f:
        real_content = base64.b64encode(f.read())
    
    base64_ref_image = ref_content.decode('utf-8')
    base64_real_image = real_content.decode('utf-8')

    return (answer_class, predict_class, base64_ref_image, base64_real_image)