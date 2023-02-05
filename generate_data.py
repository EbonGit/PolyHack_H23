import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

nTops = 4
nBottoms = 4
nShoes = 4

def init():

    df = pd.read_csv('Prefab.csv')
    df.to_csv('out.csv', index=False)

    # df = pd.DataFrame({'top': [], 'bottom': [], 'shoes': [], 'result': []})
    # print(df.describe())
    #
    # for i in range(1, 5):
    #     for j in range(1, 5):
    #         for k in range(1, 5):
    #             new_row = pd.DataFrame({'top': [i], 'bottom': [j], 'shoes': [k], 'result': [-1]})
    #             df = pd.concat([df, new_row])
    #
    # print(df.describe())
    # df = df.fillna(0)
    # df = df.astype(int)
    # df = df.sample(frac=1).reset_index(drop=True)
    # df.to_csv("out.csv", index=False)

def reset():
    df = pd.read_csv('Prefab_2.csv')
    df.to_csv('out.csv', index=False)

if __name__ == "__main__":
    init()