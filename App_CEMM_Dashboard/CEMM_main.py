# Original

import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import sys
from pathlib import Path
from cemm_lib import visual_rep_mod as visual
from cemm_lib import data_con_mod as data_manager
from cemm_lib import data_cleansing as cleansing
from dash.exceptions import PreventUpdate

#from cemm_lib import data_cleansing as dcleanse

from dash.dependencies import Input, Output, State

import os

#=== Imports for Upload function ====
import base64
import datetime
import io


#========================
# CONFIG
enable_dataConnection = False
#=================

file_name="dub_rent_missing.csv"
datafolder=Path("Data")
csv_file = open(datafolder/file_name)
df = pd.read_csv(csv_file)

print("#45 START: printing df ")
print(df)
print("#45 END")

org_raw_df = df
df_obj = cleansing.obj_list_of_missing_values(df)

itemx_state = ""

global post_cleaning_df
post_cleansing_df= df

# DEBUG PRINT:
# // print("\n #16 : ")

#Fix_this --  DETAIL: Make varlist for this
list_of_row_column_pair = []
""" ^
> List (L0) -- list of tupples
    ^ Tupple (L1)
        > row
        > column
"""
list_of_radio_items_id = []
list_of_rd_value=[]

global varlist_df_obj
varlist_df_obj=[]
varlist_df_obj.clear()
varlist_df_obj.append(df_obj)

global varlist_post_cleansing_df
varlist_post_cleansing_df=[]

dbn = 0
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ====  Upload Method ====
def parse_contents(contents, filename, date):
    print("#43 START: parse_contents() \n")
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        print("\n -> parse_contents() -> try: \n")
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            print("#46 Processing csv file")
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            print("#47 Processing excel file")
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print("#44 ERROR: Error during parsing \n")
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    print("#48 START: Printing df \n")
    print(df)
    print("#48 END \n")

    df_obj = cleansing.obj_list_of_missing_values(df)

    print("#43 END: parse_contents() \n")
    return extractor__to_html_row(df_obj)

#===============================


def update_post_cleansing_df():

    print("\n #21 START: --> Activated: updated_post_cleaning_df")
    temp_df = df
    temp_list_rd_input = list_of_rd_value

    print("\n #25 \n", list_of_rd_value,"\n")
    print("#50 START: Printing list_of_row_column_pair")
    print(list_of_row_column_pair)
    print("#50 END: Printing list_of_row_column_pair")

    # LOOP - go through
    # try:
    print("\n #23 START --> Activated: loop ")
    n_index = 0
    for row_col in list_of_row_column_pair:

        print("\n #26 Looping :", n_index)
        row = row_col[0]
        col = row_col[1]
        cell_input_value = temp_list_rd_input[n_index]

        # DELETE
        if(cell_input_value == "del"):
            temp_df = temp_df.drop([row], axis=0)
            print("\n #28 delete at loop ", n_index)

        n_index = n_index + 1

    print("\n #23 END --> Activated: loop ")

    """
    except Exception as e:
        print("\n #25 Exception: ", e)
        print("\n #24 --> Exception activated ")
        temp_df = df
    """

    # Reset Index
    temp_df = temp_df.reset_index(drop=True)

    print("")

    print("#32 START: Updating the dataframe [post_cleansing_df]")
    #print("#33 START: Displaying the old post_cleansing_df...")
    #print(post_cleansing_df)
    #print("33 END")

    print("#34 START: Updating the post_cleansing_df")
    post_cleansing_df = temp_df
    print("#34 END: Updating the post_cleansing_df")
    print("Printing the new post_cleansing_df")
    print(post_cleansing_df)

    varlist_post_cleansing_df.clear()
    varlist_post_cleansing_df.append(post_cleansing_df)

    print("#42 START: Printing varlist_post_cleansing_df[0]: \n")
    print(varlist_post_cleansing_df[0])
    print("#42 END")

    print("#32 END: Updating the dataframe [post_cleansing_df]")

    print("\n #21 END: --> Activated: updated_post_cleaning_df")

#DESCRIPTION:
#   Returns a HTML Object that displays all the  value row
#   each row has a radio-button for options -- ignore, delete, replace.
def extractor__to_html_row(obj__value):
    print("#49 START extractor__to_html_row()")
    this_df = obj__value[0]
    list_of_rows = obj__value[1]
    n_row = 0
    row_col_id = ""

    table_head =[]

    list_of_tr_item =[]
    list_of_rd_input=[]
    #// list_of_this_pair=[] # A Local Storage for cell x,y coordination

    for k in list_of_rows:
        listOf_cell = list_of_rows[n_row]
        list_of_row_radio_items = []
        list_x1 = []
        # print("\n -> extractor() --> for k in list_of_rows : ", n_row ,"\n")
        # print("\n -> extractor() --> for k in list_of_rows --> printing this_cell ", this_cell ,"\n")

        print("\n -> extractor()"
            " \n --> for k in list_of_rows"
        )

        #=====================
        # DESC:  Loops through each column-cells in a row:
        n_cell = 0 # n_cell -- column cell (left to right)
        for this_cell in listOf_cell:
            cell_index = this_cell[0] # L4-1
            cell_index_x = cell_index[0] #L5-1
            cell_index_y = cell_index[1] #L5-2

            cell_value = this_cell[2]

            print("\n -> extractor()",
                " \n --> for k in list_of_rows"
                "\n --> for this_cell in  listOf_cell"
                 ,this_cell ,"\n"
            )

            if this_cell[1] == False:
                bg_cell = "rgb(255, 179, 153)"
                row_col_id = str(cell_index_x)+"_"+str(n_cell)
                list_of_row_column_pair.append((cell_index_x,n_cell))
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
            n_cell = n_cell + 1
        # END (for this_cell in listOf_cell)

        list_x3 = [
            dcc.RadioItems(
                id = 'radioitem_'+str(row_col_id),
                options=[
                     {'label': 'Ignore', 'value': 'ign'},
                     {'label': 'Delete', 'value': 'del'}
                ],
                value='ign',
                labelStyle={'display': 'inline-block'}
            ),
            #// add_to_bt_itemlist(component_id, component_value)
            print("\n #16 \n"),
            list_of_radio_items_id.append('radioitem_'+str(row_col_id)),
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

    # DESCRIPTION:
    #   Table -- with rows of  value + option buttons
    html_table =html.Table(
        [
            html.Tr([html.Th(col) for col in this_df.columns])
        ]
        +
        list_of_tr_item
    )

    html_output = html.Div(
        [
            html_table,
            html.Button('Apply', id='apply_btn')
        ],
    )

    L2_3 = obj__value[2]
    data_is_clean = L2_3[1]

    # DEBUG PRINT:
    print("\n extractor__to_html_row() #14 :")
    print("> data_is_clean = ", data_is_clean)

    if data_is_clean == True :
        html_output = html.Div(
            children="Data is valid and clean"
        )

    # DEBUG PRINT:
    print("\n printing the object: \n")
    print(obj__value)
    print("\n printing the return: \n")
    print(html_table)
    print("\n")
    print("#49 END extractor__to_html_row()")
    return html_output

def dcleanse_table(df):
    dataframe = df
    start_n = 0

    #rows_with__value = dcc.

    return html.Div(
        html.Table(
            [
                html.Tr([html.Th(col) for col in dataframe.columns])
            ]
            +
            # Body
            [
                html.Tr(
                    [
                        html.Td(
                            dataframe.iloc[i][col],
                            # - Style attribute
                            style={
                                'backgroundColor':'yellow'
                            }
                        ) for col in dataframe.columns
                    ]
                    +
                    [ # NOTE: Additional objects here for each row:
                        dcc.RadioItems(
                            # REMINDER: Put ID here
                            options=[
                                  {'label': 'Ignore', 'value': 'ign'},
                                  {'label': 'Delete', 'value': 'del'}
                            ],
                            style={
                                "value": "ign",
                                "display":"inline-block"
                            },
                            value='ign',
                            labelStyle={'display': 'inline-block'}
                        ),
                    ],
                ) for i in range(len(dataframe))
            ],
        )
    )

def add_to_bt_itemlist(radio_item, id):

    return

# DESCRIPTION:
#   A function that takes the value of each radio-button item.
# RETURNS:
#   Returns A list of the value of each radio-button item
def callback_loop_radioitem_id():
    print("\n #30 START : callback_loop_radioitem_id() activated")
    list_of_rd_input=[]
    for item in list_of_radio_items_id :
        list_of_rd_input.append(State(item,'value'))

    print("\n #18 ",list_of_rd_input,"\n")
    return list_of_rd_input
    print("\n #30 END : callback_loop_radioitem_id() activated")

# DESCRIPTION :
#   Modify or Deletes the row
def modify__value_row():
    return


#=====================================


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

    html.Div(
         id='output-container-button',
         children=[extractor__to_html_row(varlist_df_obj[0]),
         visual.generate_table_v2(varlist_df_obj[0][0])]
         # children = output-container-button
    ),
])


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

@app.callback(
    Output('output-container-button', 'children'),
    [Input('apply_btn', 'n_clicks')],
    callback_loop_radioitem_id()
    #// callback_loop(),
)
def update_output(n_clicks, *radio_item_value_id):
    if n_clicks is None:
        raise PreventUpdate
    else:
        print("\n -> #3 update_output_div()\n \"Apply\" button has been pressed ")

        returnx = ""
        # Print Debug:
        print("#13 START printing value:")
        print(radio_item_value_id)
        print("#13 END \n")

        print("\n #27 --> Clearing list")
        list_of_rd_value.clear()

        for item in radio_item_value_id:
            list_of_rd_value.append(item)

        print("#31 START: update_post_cleansing_df() ")
        update_post_cleansing_df()
        print("#31 END: update_post_cleansing_df() ")

        print("#41 START: printing varlist_post_cleansing_df[0]: ")
        print(varlist_post_cleansing_df[0])
        print("#41 END")

        # ERROR : Not displaying the updated dataframe
        return(
            visual.generate_table_v2(varlist_post_cleansing_df[0])
        )



if __name__ == '__main__':
    app.run_server(debug=True)
    app.config.suppress_callback_exceptions = True
