import pandas as pd
import numpy as np
import os
print("Colaboradores")
print("1 -> Sofi , 2 -> Juanjo, 3 -> Sebas")
print("por fin mkis")
a=""
numero= input("Numero de quien corre:")
if numero=="1":
    a="C:\\Users\\asbar\\OneDrive - Universidad de los Andes\\Carrera\\Séptimo semestre 2023-1\\ANALITICA\\Proyecto_1actd\\processed.cleveland_repaired.csv"
elif numero =="2":
    a= "C:\\Users\\JUAN JOSE F ROMERO\\Documents\\UNIANDES\\2023-01\\Analítica Comp\\Proyecto_1actd\\processed.cleveland_repaired.csv"
else:
    a="C:\\Users\\juanc\\Documents\\ANDES\\2023-1\\Analitica\\Proyecto_1actd\\processed.cleveland_repaired.csv"

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

#Histograma de la presion arterial

plt.hist(trestbps, bins=10, color='#800080',edgecolor='black', alpha=0.7)
plt.title('Distribución de la presión arterial')
plt.xlabel('presión arterial')
plt.ylabel('Frecuencia')

media = np.mean(trestbps)
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()

#Grafico de dispersion chol

plt.scatter(edades, chol)

# agregar etiquetas y título
plt.xlabel('Edades')
plt.ylabel('Colesterol')
plt.title('Gráfico de dispersión del chol')

# mostrar el gráfico
plt.show()

#Grafico de dispersion fbs

plt.scatter(edades, trestbps, color="green")

# agregar etiquetas y título
plt.xlabel('Edades')
plt.ylabel('presión arterial')
plt.title('Gráfico de dispersión de la presión arterial dado la edad')

# mostrar el gráfico
plt.show()



import seaborn as sns


# Crear el gráfico de violín sexo y chol
sns.violinplot(x="sex", y="chol", hue="sex", data=data, split=True)

# Personalizar el gráfico (opcional)
plt.title('Gráfico de violín')
plt.xlabel('Día')
plt.ylabel('Total de la factura')

plt.show()
