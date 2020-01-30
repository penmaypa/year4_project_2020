import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#displayDiv = 'display'

displayDiv='block'

app.layout = html.Div([
    html.Button('Click here to see the content', id='show-secret'),

    html.Div(id='body-div',
        children='This is test',
        style={
            'backgroundColor':'rgb(112, 180, 255, 0.5)',
            'display': displayDiv
        }
    )
])

@app.callback(
    Output(component_id='body-div', component_property='children'),
    [Input(component_id='show-secret', component_property='n_clicks')]
)

def update_output(n_clicks):
    print(n_clicks)
    if n_clicks is None:
        shown = True
        print("shown = true")
        raise PreventUpdate
    else:
        return html.Script(alert('If you see this alert, then your custom JavaScript script has run!'))

        """
        if (n_clicks % 2) == 0:
           return html.Div(
                style={
                        'display':'none'
                    }
               )
        else:
           return html.Div(
                style={
                        'display':'block'
                    }
               )
              """



if __name__ == '__main__':
    app.run_server(debug=True)
