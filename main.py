import seaborn as sns
import matplotlib.pyplot as plt
import random
import csv
import pandas as pd


df = pd.DataFrame({'Utilisé (1/0)': []})
for i in range(360):
    df['Utilisé (1/0)'][i] = random.randint(0,1)
ValeursParMois = []
somme = 0
for i in range(0,30):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(30,60):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(60,90):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(90,120):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(120,150):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(150,180):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(180,210):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(210,240):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(240,270):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(270,300):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(300,330):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)
somme = 0
for i in range(330,360):
    somme += int(df['Utilisé (1/0)'][i])
    ValeursParMois.append(somme)

listeMois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
print(ValeursParMois)






























