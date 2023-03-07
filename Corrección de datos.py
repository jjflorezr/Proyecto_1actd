import pandas as pd
import numpy as np
import os

a=""
ejecutador= input("Quien esta corriendo?")
if ejecutador=="Sofia":
    a="C:\\Users\\asbar\\OneDrive - Universidad de los Andes\\Carrera\\Séptimo semestre 2023-1\\ANALITICA\\Proyecto_1actd\\processed.cleveland.data"

data = pd.read_csv(a)
print(data.head())


data.replace("?", np.nan, inplace=True)

# Convertimos todas las columnas a tipo float para poder calcular el promedio
data = data.astype(float)

# Calculamos el promedio de la columna "ca", excluyendo los valores faltantes
ca_mean = data["ca"].mean(skipna=True)

# Reemplazamos los valores faltantes en la columna "ca" con el promedio
data["ca"].fillna(ca_mean, inplace=True)

# Guardamos los datos en un nuevo archivo
data.to_csv("processed.cleveland_repaired.csv", index=False, header=None)

print("y mi regalo?")
