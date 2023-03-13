import dash 
import dash_core_components as dcc
import dash_html_components as html


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
    html.H1('Prevención de enfermedades gastrovasculares'),
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
              (id='my-input', value='', type='text')]),
    html.Br(),
    html.Div(id='output')
])

sexo=""
edad=""
col =""

@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('dropdown', 'value')],
    [dash.dependencies.Input('my-input','value')],
    
    )



def update_output(dropdow_value,input_value):
    global sexo
    sexo = dropdow_value
    if sexo=="Hombre":
        sexo=1
    else:
        sexo=0
    global edad
    edad= input_value
    
    #return 'Eres "{}" y tu edad es "{}"'.format(sexo, edad)
    return html.Div([
        html.H4(f"Tu sexo es : {int(sexo)}"),
        html.H4(f"Tu edad es: {edad}"),
        
    ])



<<<<<<< HEAD

=======
def update_output(value):
    print(value)
    
    return 'Has seleccionado "{}"'.format(value)
>>>>>>> 8a39945642ce3ad102352c3145488319a5ea90cd



if __name__ == '__main__':
    app.run_server(debug=True)
