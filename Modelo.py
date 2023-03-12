import pandas as pd
import numpy as np
import os
from pgmpy.models import BayesianModel
from pgmpy.sampling import BayesianModelSampling
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
from pgmpy.inference import VariableElimination

df = pd.read_csv('heart_disease_modified.csv')

model = BayesianModel([('age','chol'),('age','fbs'),('sex','chol'),('sex','fbs')
                      ,('chol','num'),('fbs','num')
                      , ('num','cp'), ('num','exang'), ('num','anom_thalach'), ('num','trestbps')])

model.fit(df, estimator=MaximumLikelihoodEstimator)

for i in model.nodes():
    print(model.get_cpds(i))

#PRUEBA INFERENCIA
infer = VariableElimination(model)
P1 = infer.query(['num'], evidence={'age': '0-45','sex':1, 'chol':'0-240','fbs':1})
print(P1)