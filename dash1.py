import dash 
import dash_core_components as dcc
import dash_html_components as html

app= dash.Dash()

#app.layout = html.Div([
 #   html.H1('Mi tablero de Dash'),
  #  html.Div([
   #     html.P('Este es un párrafo de texto.'),
      #  html.P('Este es otro párrafo de texto.')
    #])
#])

#if __name__ == '__main__':
 #   app.run_server()



options = [
    {'label': 'Hombre', 'value': 'Hombre'},
    {'label': 'Mujer', 'value': 'Mujer'},
    
]

app.layout = html.Div([
    html.H1('Mi tablero de Dash'),
    html.Div([
      html.P('Seleccione su sexo.')]),
    dcc.Dropdown(
        id='dropdown',
        options=options,
        value='Hombre'
    ),
    html.H3("¿Qué edad tiene?"),
    html.Div(["Edad: ",
              dcc.Input(id='my-input', value='valor inicial', type='text')]),
    html.Br(),
    html.Div(id='my-output')
])

@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('dropdown', 'value')])

def update_output(value):
    print(value)
    
    return 'Has seleccionado "{}"'.format(value)



if __name__ == '__main__':
    app.run_server()