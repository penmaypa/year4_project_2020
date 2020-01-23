import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from cemm_lib import visual_rep_mod as visual

from dash.dependencies import Input, Output

import os
#from app import app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


#df = visual.read_this_csv("Data/emp2017.csv")
#df = "empty"
df = visual.read_this_csv("Data/dub_rent.csv")

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div(
        [
            html.H1(children='CEMM Dashboard',
                style={
                    'textAlign':'center',
                    'font-weight':'bold'
                },
            ),
            html.H4(
                children="Country's Economy Monitoring and Managment Dashboard",
                style={
                    'textAlign':'center',
                    'font-weight':'bold'
                },
            )
        ],
        style={
            'backgroundColor':'rgb(112, 180, 255, 0.5)'
        }
    ),

    # === Callback test ====

    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div'),

    # === Visual Representation here ===
    visual.generate_table("Employment 2017",df),
    visual.generate_barChart("Employment 2017",df),
    # fig.show()
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)

def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)



if __name__ == '__main__':
    app.run_server(debug=True)
    app.config.suppress_callback_exceptions = True
