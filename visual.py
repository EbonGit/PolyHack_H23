import random

import matplotlib.pyplot as plt

annee = []
for j in range(12*30):
    annee.append(random.randint(0, 1))

somme_annee = 0
for j in annee:
    somme_annee += annee[j]

mois = []
for i in range(12):
    somme_mois = 0
    for j in range(i*30, (i*30) + 30):
        somme_mois += annee[j]
    mois.append(somme_mois)
print(mois)
plt.plot(mois)
plt.show()