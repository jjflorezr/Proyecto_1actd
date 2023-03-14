import pandas as pd
import numpy as np
import os
print("Colaboradores")
print("1 -> Sofi , 2 -> Juanjo, 3 -> Sebas")

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
plt.xticks([1, 2, 3,4], nombres_variables)
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

#Histograma de la presion arterial en reposo

plt.hist(trestbps, bins=10, color='#800080',edgecolor='black', alpha=0.7)
plt.title('Distribución de la presión arterial en reposo')
plt.xlabel('presión arterialen reposo (mm Hg)')
plt.ylabel('Frecuencia ')

media = np.mean(trestbps)
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()

#Histograma del colesterol

plt.hist(chol, bins=10, color='#ADD8E6',edgecolor='black', alpha=0.7)
plt.title('Distribución del colesterol')
plt.xlabel('Colesterol mg/dl')
plt.ylabel('Frecuencia')

media = np.mean(chol)
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()

#Histograma de la frecuencia cardiaca

plt.hist(thalach, bins=10, color='#90EE90',edgecolor='black', alpha=0.7)
plt.title('Distribución de la frecuencia cradiaca en reposo')
plt.xlabel('Frecuencia cardiaca')
plt.ylabel('Frecuencia')

media = np.mean(thalach)
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()


#Grafico de dispersion chol dada la edad

plt.scatter(edades, chol)
plt.xlabel('Edades')
plt.ylabel('Colesterol')
plt.title('Gráfico de dispersión del chol(mg/dl) dado la edad')
plt.show()

#Grafico de dispersion presion arterial dada la edad

plt.scatter(edades, trestbps, color="green")
plt.xlabel('Edades')
plt.ylabel('Presión arterial (mm Hg)')
plt.title('Gráfico de dispersión de la presión arterial dado la edad')
plt.show()

#Grafico de thalac  dada la edad

plt.scatter(edades, thalach, color="red")
plt.xlabel('Edades')
plt.ylabel('Frecuencia cardiaca')
plt.title('Gráfico de dispersión de la frecuencia cardiaca dado la edad')
plt.show()


# mostrar el gráfico
plt.show()



import seaborn as sns

# Crear el gráfico de violín sexo y chol
sns.violinplot(x="sex", y="chol", hue="sex", data=data, split=True)

# Personalizar el gráfico (opcional)
plt.title('Gráfico del colesterol de acuerdo al sexo')
plt.xlabel('sexo')
plt.ylabel('chol')

plt.show()

sns.violinplot(data=todos)
plt.xticks([0, 1, 2,3], nombres_variables)
plt.title('Distribución de las variables age, trestbp, chol,thalach ')
plt.show()


# Crear el gráfico de violín threst y chol
sns.violinplot(x="fbs", y="age", hue="sex", data=data, split=True)

# Personalizar el gráfico (opcional)
plt.title('Distribución de la edad de acuerdo al sexo y fasting blood sugar > 120 mg/dl')
plt.xlabel('fbs')
plt.ylabel('edad')

plt.show()

