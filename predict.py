import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import random

np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

def binaries_concat(top, bottom, shoes):
    i1 = str(hex(top)).split("x")[1] + str(hex(bottom)).split("x")[1] + str(hex(shoes)).split("x")[1]
    i2 = str(hex(bottom)).split("x")[1] + str(hex(shoes)).split("x")[1] + str(hex(top)).split("x")[1]
    i3 = str(hex(shoes)).split("x")[1] + str(hex(top)).split("x")[1] + str(hex(bottom)).split("x")[1]
    return (int("0x" + i1, 16), int("0x" + i2, 16), int("0x" + i3, 16))


def result_analyse(result):
  a = result[0][0]
  if(a < 0):
    return 0
  elif(a > 1):
    return 1
  else:
    return round(a)

def predict_model(top, bottom, shoes):
    model = keras.models.load_model('model.h5')

    top_, bottom_, shoes_ = binaries_concat(top, bottom, shoes)

    return result_analyse(model.predict([top_,bottom_,shoes_]))