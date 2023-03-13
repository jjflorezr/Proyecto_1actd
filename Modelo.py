import pandas as pd
import numpy as np
import os
from pgmpy.models import BayesianModel
from pgmpy.sampling import BayesianModelSampling
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
from pgmpy.inference import VariableElimination

print("Colaboradores")
print("1 -> Sofi , 2 -> Juanjo, 3 -> Sebas")

a=""
numero= input("Numero de quien corre:")
if numero=="1":
    a="C:\\Users\\asbar\\OneDrive - Universidad de los Andes\\Carrera\\Séptimo semestre 2023-1\\ANALITICA\\Proyecto_1actd\\heart_disease_modified.csv"
elif numero =="2":
    a= "C:\\Users\\JUAN JOSE F ROMERO\\Documents\\UNIANDES\\2023-01\\Analítica Comp\\Proyecto_1actd\\heart_disease_modified.csv"
else:
    a="C:\\Users\\juanc\\Documents\\ANDES\\2023-1\\Analitica\\Proyecto_1actd\\heart_disease_modified.csv"

df = pd.read_csv(a)

model = BayesianModel([('age','chol'),('age','fbs'),('sex','chol'),('sex','fbs')
                      ,('chol','num'),('fbs','num')
                      , ('num','cp'), ('num','exang'), ('num','anom_thalach'), ('num','trestbps')])

model.fit(df, estimator=MaximumLikelihoodEstimator)

for i in model.nodes():
    print(model.get_cpds(i))

#PRUEBA INFERENCIA

edad="0-45"
infer = VariableElimination(model)
P1 = infer.query(['num'], evidence={'age': edad,'sex':1, 'chol':'0-240','fbs':1})
print(P1)


