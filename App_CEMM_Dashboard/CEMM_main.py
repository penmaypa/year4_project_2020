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

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    # Headings
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
            ),
            html.Div(
                style={
                    'height':'5px'
                }
            )
        ],
        style={
            'backgroundColor':'rgb(112, 180, 255, 0.5)'
        }
    ),

    # === Upload ====
    html.Div(
        [
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=True
            ),
            html.Div(id='output-data-upload'),
        ]
    ),

    # === Visual Representation here ===
    visual.generate_table("Employment 2017",df),
    visual.generate_barChart("Employment 2017",df),
    # fig.show()
])


if __name__ == '__main__':
    app.run_server(debug=True)
    app.config.suppress_callback_exceptions = True
