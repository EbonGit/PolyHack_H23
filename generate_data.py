import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

nTops = 10
nBottoms = 12
nShoes = 6

df = pd.DataFrame({'top': [], 'bottom': [], 'shoes': [], 'result': []})
print(df.describe())

for j in range(200):
    top = random.randint(1, nTops)
    bottom = random.randint(1, nBottoms)
    shoes = random.randint(1, nShoes)

    result = 0

    if ((top + bottom + shoes) % 2 == 0):
        result = 1

    new_row = pd.DataFrame({'top' : [top], 'bottom' : [bottom], 'shoes' : [shoes], 'result' : [result]})
    df = pd.concat([df, new_row])

print(df.describe())
df.to_csv("out.csv", index=False)