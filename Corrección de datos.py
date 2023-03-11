import pandas as pd
import numpy as np
import os

a=""
ejecutador= input("Quien esta corriendo?")
if ejecutador=="sofia":
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

#Graficas descriptivas

import matplotlib.pyplot as plt

# Variables
edades= data['age'].tolist()
sex=data['sex'].tolist()
cp= data['cp'].tolist()
trestbps= data['trestbps'].tolist()
chol= data['chol'].tolist()
fbs= data['fbs'].tolist()
restecg= data['restecg'].tolist()
thalach= data['thalach'].tolist()
exang= data['exang'].tolist()
oldpeak= data['oldpeak'].tolist()
slope= data['slope'].tolist()
ca= data['ca'].tolist()
thal= data['thal'].tolist()
num= data['num'].tolist()

# Diagramas de caja para edades,trestbps,chol,thalach

todos=[edades,trestbps,chol,thalach]
plt.boxplot(todos)

plt.title('Diagrama de Caja')
plt.xlabel('Variables')
plt.ylabel('Valores')

nombres_variables = ['age', 'trestbp', 'chol','thalach']
plt.xticks([1, 2, 3, 4], nombres_variables)
plt.show()

#Histograma de la edad

plt.hist(edades, bins=10, color='#E69F00',edgecolor='black', alpha=0.7)
plt.title('Distribución de la edad')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

media = np.mean(edades)
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()

#Diagrama de barras de sexo

femenino=0
masculino=0

for i in sex:
    if i==0:
        femenino= femenino+1
    else:
        masculino= masculino +1

nombres = ['Hombres', 'Mujeres']
valores = [masculino,femenino]

# Crear el diagrama de barras
plt.bar(nombres, valores)

# Personalizar el gráficoS
plt.title('Grafico de barras')
plt.xlabel('Sexo')
plt.ylabel('Cantidad')

# Mostrar el gráfico
plt.show()
