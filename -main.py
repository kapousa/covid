import os

from keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
model = load_model('static/model/covid_vgg.h5')
import numpy as np


