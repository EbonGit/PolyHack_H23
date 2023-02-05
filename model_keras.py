import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import predict

import random

np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

def binaries_concat(top, bottom, shoes):
    i1 = str(hex(top)).split("x")[1] + str(hex(bottom)).split("x")[1] + str(hex(shoes)).split("x")[1]
    i2 = str(hex(bottom)).split("x")[1] + str(hex(shoes)).split("x")[1] + str(hex(top)).split("x")[1]
    i3 = str(hex(shoes)).split("x")[1] + str(hex(top)).split("x")[1] + str(hex(bottom)).split("x")[1]
    return (int("0x" + i1, 16), int("0x" + i2, 16), int("0x" + i3, 16))

#binaries_concat(1, 3, 11)

def result_analyse(result):
  a = result[0][0]
  if(a < 0):
    return 0
  elif(a > 1):
    return 1
  else:
    return round(a)

def build_model(norm):
  model = keras.Sequential([
      norm,
      layers.GaussianNoise(0.1, seed=None),
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
  ])
  model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model

def main():

    url = 'out.csv'
    raw_dataset = pd.read_csv(url, header = 0,
                              na_values='?', comment='\t',
                              sep=',', skipinitialspace=True)

    dataset = raw_dataset.copy()
    dataset = dataset.dropna()

    data_tab = []
    for index, row in dataset.iterrows():
        top, bottom, shoes = binaries_concat(round(row["top"]), round(row["bottom"]), round(row["shoes"]))
        data_tab.append([top, bottom, shoes, row["result"]])

    dataset_ = pd.DataFrame(data_tab)
    dataset_.columns = ["top", "bottom", "shoes", "result"]

    train_copy = dataset_.copy()
    train_labels = train_copy.pop('result')

    train_features = train_copy[["top", "bottom", "shoes"]]

    features_normalizer = layers.Normalization(axis=-1)
    features_normalizer.adapt(train_features)




    model = build_model(features_normalizer)


    history = model.fit(
        train_features,
        train_labels,
        validation_split=0.2,
        verbose=1, epochs=100)
    save_format = 'tf'
    model.save('model')

    predict.load_model()



