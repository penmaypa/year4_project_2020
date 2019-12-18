import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import visual_rep_mod as visual

import os
#from app import app


df = visual.read_this_csv("Data/emp2017.csv")

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
#fig.show()



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

    visual.generate_table("Employment 2017",df),

    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': ['SF', 'TX'], 'y': [4, 7], 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'plot_bgcolor': 'blue',
                'paper_bgcolor': 'red',
                'font': {
                    'color': 'black'
                }
            }
        }
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)
    app.config.suppress_callback_exceptions = True
