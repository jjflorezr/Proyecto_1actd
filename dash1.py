import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import os
import csv 
from pgmpy.models import BayesianModel
from pgmpy.sampling import BayesianModelSampling
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
from pgmpy.inference import VariableElimination

df = pd.read_csv("C:\\Users\\asbar\\OneDrive - Universidad de los Andes\\Carrera\\Séptimo semestre 2023-1\\ANALITICA\\Proyecto_1actd\\heart_disease_modified.csv")

model = BayesianModel([('age','chol'),('age','fbs'),('sex','chol'),('sex','fbs')
                      ,('chol','num'),('fbs','num')
                      , ('num','cp'), ('num','exang'), ('num','anom_thalach'), ('num','trestbps')])

model.fit(df, estimator=MaximumLikelihoodEstimator)

#for i in model.nodes():
 #   print(model.get_cpds(i))

#PRUEBA INFERENCIA


#PRUEBA INFERENCIA - Ya separdo el valor, para poder hacer un IF con la recomendacion


#COMIENZA DASH
app= dash.Dash()




options_sexo= [
    {'label': 'Hombre', 'value': 'Hombre'},
    {'label': 'Mujer', 'value': 'Mujer'},
    
]
options_col=[
    {'label':'0-240','value':'0-240'},
    {'label':'240-260','value':'240-260'},
    {'label':'260-400','value':'260-400'}
    ]


app.layout = html.Div([
    html.H1('Prevención de enfermedades cardiovasculares'),
    html.Div([
      html.P('Seleccione su sexo.')]),
    dcc.Dropdown(
        id='dropdown',
        options=options_sexo,
        value='Hombre'
        ),
    html.Div(id='output'),
    html.P("¿Qué edad tiene?"),
    html.Div(["Edad: ",
              dcc.Input
              (id='my-input', value='0', type='text')]),
    html.Br(),
    html.Div(id='output'),
    html.Div([
      html.P('Seleccione su nivel de colesterol mg/dl.')]),
    dcc.Dropdown(
        id='dropdown_col',
        options=options_col,
        value=''
        ),
        html.Button('Enviar', id='button'),
        html.Br(),
        html.Div(id='output')
])

sexo=""
edad=""
col =""
proba=0
@app.callback(dash.dependencies.Output('output', 'children'),
              [dash.dependencies.Input('button', 'n_clicks')],
              [dash.dependencies.State('dropdown', 'value')],
              [dash.dependencies.State('my-input', 'value')],
              [dash.dependencies.State('dropdown_col', 'value')]
              )

def update_output(n_clicks, dropdow_value,input_value,dropdown_col):
      global sexo
      sexo = dropdow_value
      if sexo=="Hombre":
          sexo=1
      else:
          sexo=0
      global edad
      edad= input_value
      if int(edad)<=44:
        edad="0-45"
      elif int(edad)<=54:
        edad="45-55"
      else:
        edad='55-100'
    
      global col
      col= dropdown_col
      global proba
      infer = VariableElimination(model)
      P1 = infer.query(['num'], evidence={'age': edad,'sex':sexo, 'chol':col,'fbs':1})
      proba= P1.values
      if proba[0]>0.3:
         recomendacion="Deberias ir al médico"
      return html.Div([
      html.H4(f"Tu sexo es : {int(sexo)}"),
        html.H4(f"Tu edad es: {edad}"),
        html.H4(f"Su colesterol es: {col}"),
        html.H4(f"Tu probabilidad: {proba[0]}"),
        html.H4(f"{recomendacion}")])
        


if __name__ == '__main__':
    app.run_server(debug=True)

