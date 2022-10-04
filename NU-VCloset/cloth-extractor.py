import os
from io import BytesIO
import tarfile
import tempfile
from six.moves import urllib

from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

# silent warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

MODEL_NAME = 'frozen_inference_graph-110871.pb'
MODEL_DIR = os.path.join(BASE_DIR, "models", "deeplab")
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)


MODEL_NAME = 'frozen_inference_graph-110871.pb'
MODEL_DIR = os.path.join(BASE_DIR, "models", "deeplab")
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)


LABEL_NAMES = np.asarray(['BG', 'short_sleeved_shirt', 'long_sleeved_shirt',
                          'short_sleeved_outwear', 'long_sleeved_outwear',
                          'vest', 'sling', 'shorts', 'trousers', 'skirt', 'short_sleeved_dress',
                          'long_sleeved_dress', 'vest_dress', 'sling_dress'])

FULL_LABEL_MAP = np.arange(1, len(LABEL_NAMES)+1).reshape(len(LABEL_NAMES), 1)
# print(FULL_LABEL_MAP)
