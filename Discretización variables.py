import pandas as pd
import numpy as np
import os

from pgmpy.sampling import BayesianModelSampling
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Leer la base de datos de enfermedades del corazón
df = pd.read_csv("processed.cleveland_repaired.csv")

#Añadir columna que indica anomalía, asignar valores = 1 si hay, 0 si no

df["anom_thalach"] = 0
df.loc[(220 - df["age"]) < df["thalach"], "anom_thalach"] = 1

# Discretizar la edad en 3 grupos
df['age'] = pd.cut(df['age'], bins=[0, 45, 55, 100], labels=['0-45', '45-55', '55-100'])

# Discretizar la presión en 3 grupos
df['trestbps'] = pd.cut(df['trestbps'], bins=[0, 120, 140, 300], labels=['0-120', '120-140', '140-300'])

# Discretizar el colesterol en 3 grupos
df['chol'] = pd.cut(df['chol'], bins=[0, 240, 260, 400], labels=['0-240', '240-260', '260-400'])

# Discretizar el Oldpeak en 2 grupos
df['oldpeak'] = pd.cut(df['oldpeak'], bins=[0, 0.5, 6.2], labels=['0-0.5', '0.5-6.2'])

#Cambiar valores en target por 1 o 0
df['num'] = df['num'].replace([1, 2, 3, 4,0], [1, 1, 1,1, 0])

#Borrar columnas sin usar

del df['restecg']
del df['oldpeak']
del df['slope']
del df['ca']
del df['thal']
# Verificar los cambios
print(df.head())
df.to_csv('heart_disease_modified.csv', index=False)