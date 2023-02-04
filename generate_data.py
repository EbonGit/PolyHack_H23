import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

nTops = 4
nBottoms = 4
nShoes = 4

df = pd.DataFrame({'top': [], 'bottom': [], 'shoes': [], 'result': []})
print(df.describe())

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            new_row = pd.DataFrame({'top': [i], 'bottom': [j], 'shoes': [k], 'result': [-1]})
            df = pd.concat([df, new_row])

print(df.describe())
df = df.fillna(0)
df = df.astype(int)
df.to_csv("out.csv", index=False)