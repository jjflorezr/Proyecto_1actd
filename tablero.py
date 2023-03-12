# -*- coding: utf-8 -*-

# Ejecute esta aplicación con 
# python app1.py
# y luego visite el sitio
# http://127.0.0.1:8050/ 
# en su navegador.


import dash
from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# en este primer ejemplo usamos unos datos de prueba que creamos directamente
# en un dataframe de pandas 
df = pd.DataFrame({
    "Materias": ["Analitica", "Teoria", "TI", "Analitica", "Teoria", "TI","Analitica", "Teoria", "TI"],
    "Nota": [5, 4, 2, 5, 2, 4, 5 ,2 ,3],
    "Estudiante": ["Sebas", "Sebas", "Sebas", "Sofi", "Sofi", "Sofi","Juanjo","Juanjo","Juanjo"]
})

fig = px.bar(df, x="Materias", y="Nota", color="Estudiante", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='El mejor tablero en Dash'),

    html.Div(children='''
        Histograma de notas estudiantes 2023-1 :)
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(children='''
        En este gráfico se observa las notas por estudiante en el semestre 2023-1.
    '''),
    html.Div(
        className="Columnas",
        children=[
            html.Ul(id='my-list', children=[html.Li(i) for i in df.columns])
        ],
    )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

