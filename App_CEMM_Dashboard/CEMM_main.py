import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from cemm_lib import visual_rep_mod as visual
from cemm_lib import data_con_mod as data_manager
#from cemm_lib import data_cleansing as dcleanse

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
    data_manager.dataset_url_manager(enable_dataConnection),
    #visual.generate_table_v3()
    #extractor__to_html_row(dcleanse.obj_list_of_missing_values(df))

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


def extractor__to_html_row(obj_missing_value):
    this_df = obj_missing_value[0]
    m.dprint("-> ... extractor()")
    list_of_rows = obj_missing_value[1]
    n_row = 0
    table_head =[]
    list_of_tr_item =[]


    for k in list_of_rows:
        listOf_cell = list_of_rows[n_row]
        list_of_row_radio_items = []
        list_x1 = []
        # print("\n -> extractor() --> for k in list_of_rows : ", n_row ,"\n")
        # print("\n -> extractor() --> for k in list_of_rows --> printing this_cell ", this_cell ,"\n")

        print("\n -> extractor()"
            " \n --> for k in list_of_rows"
        )
        # n_cell = 0
        for this_cell in listOf_cell:
            cell_index = this_cell[0]
            cell_index_x = cell_index[0]
            cell_index_y = cell_index[1]

            cell_value = this_cell[2]

            print("\n -> extractor()",
                " \n --> for k in list_of_rows"
                "\n --> for this_cell in  listOf_cell"
                 ,this_cell ,"\n"
            )

            if this_cell[1] == False:
                m.dprint("-> for k in list_of_rows --> if this cell")
                bg_cell = "rgb(255, 179, 153)"
            else:
                bg_cell = "white"


            list_x1_2=[
                html.Td(
                    cell_value,
                    style={
                        'backgroundColor' : bg_cell
                    }
                )

            ]

            list_x1 = list_x1 + list_x1_2

        # END (for this_cell in listOf_cell)
        list_x3 = [
            dcc.RadioItems(
                id = 'radioitems_'+str(cell_index_x)+'_'+str(cell_index_y),
                options=[
                     {'label': 'Ignore', 'value': 'ign'},
                     {'label': 'Delete', 'value': 'del'}
                ],
            )
        ]

        list_x4 = list_x1 + list_x3
        list_of_row_radio_items = list_of_row_radio_items + list_x4

        print("\n test_4")
        print(type(list_x1))
        print(list_x1)
        print(type(list_of_row_radio_items))

        #list_x1_tup = tuple(list_x1)

        print("\n")

        list_x2 = [html.Tr(
            list_of_row_radio_items
        )]

        list_of_tr_item = list_of_tr_item + list_x2

        print("\n test_3:")
        print(list_of_row_radio_items)
        print("\n")

        n_row = n_row + 1

    print("\n test_2 \n")
    print(list_of_tr_item)
    print("\n")

    html_table =html.Table(
        [
            html.Tr([html.Th(col) for col in this_df.columns])
        ]
        +
        list_of_tr_item
    )

    print("\n printing the object: \n")
    print(obj_missing_value)
    print("\n printing the return: \n")
    print(html_table)

    return html_table
#=====================================


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
