import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from cemm_lib import visual_rep_mod as visual

from dash.dependencies import Input, Output, State

import os

#=== Imports for Upload function ====
import base64
import datetime
import io

#from app import app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


#df = visual.read_this_csv("Data/emp2017.csv")
#df = "empty"

#df = visual.read_this_csv("Data/dub_rent.csv")

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

#========================
# CONFIG

enable_dataConnection = True

#=================

if enable_dataConnection == True:
    print("\n -> enable_dataConnection \n")
    df = pd.read_csv("https://data.smartdublin.ie/dataset/4997223b-13b2-4c97-9e88-cd94c6d35aec/resource/8c0f9bed-3b65-40c9-9bd2-505d7bdc1aeb/download/prtb-rents-ctdt.csv")
    print("-> enable_dataConnection -> printin data..."), print(df)
dbn = 0
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    # ==== Headings =====
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

    visual.generate_table_v3()
])


# ====  Upload Method ====
def parse_contents(contents, filename, date):
    print("\n -> parse_contents() \n")
    print("\n -> parse_contents() -> Printing....\n"), print("\n printing content (pre)"), print(contents), print("\n printing content (post)"), print(filename)
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        print("\n -> parse_contents() -> try: \n")
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return visual.generate_table_v2(df)

#===============================


print("\n Running Callback...\n")
@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    print("\n -> update_output()\n")
    if list_of_contents is not None:
        print("\n -> update_output() -> if: -> return() \n")
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == '__main__':
    app.run_server(debug=True)
    app.config.suppress_callback_exceptions = True
