import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from cemm_lib import visual_rep_mod as visual
from cemm_lib import misc_mod as m
from cemm_lib import data_cleansing as cleansing


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("dub_rent_missing.csv")
df_obj = cleansing.obj_list_of_missing_values(df)

itemx_state = ""


list_of_row_column_pair = []
""" ^
> List -- list of tupples
    ^ Tupple
        > row
        > column
"""
list_of_radio_items_id = []
list_of_rd_input=[]



#===========================

# DESCRIPTION:
#   Returns a HTML Object that displays all the  value row
#   each row has a radio-button for options -- ignore, delete, replace.
def extractor__to_html_row(obj__value):
    this_df = obj__value[0]
    m.dprint("-> ... extractor()")
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

    # DEBUG PRINT:
    print("\n printing the object: \n")
    print(obj__value)
    print("\n printing the return: \n")
    print(html_table)
    print("\n")

    return html_output

#======================

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
    list_of_rd_input=[]
    for item in list_of_radio_items_id :
        list_of_rd_input.append(State(item,'value'))

    print("\n #18 ",list_of_rd_input,"\n")
    return list_of_rd_input

# DESCRIPTION :
#   Modify or Deletes the row
def modify__value_row():
    return

#===================================

app.layout = html.Div([
     # dcleanse_table(df)
    extractor__to_html_row(df_obj),
    # visual.generate_table_v2(df_obj[0])
   html.Div(
        id='output-container-button',
        children="output here"
   ),

   print("\n #17 ", list_of_radio_items_id,"\n"),
   #// itemx_state = State('radioitem_12_4','value'),

  #// print("\n #12 Printing state :\n", itemx_state)

  print("\n #22"),
  print(list_of_row_column_pair),
])

@app.callback(
    Output('output-container-button', 'children'),
    [Input('apply_btn', 'n_clicks')],
    callback_loop_radioitem_id()
    #// callback_loop(),
)

def update_output(n_clicks, *radio_item_id):
    print("\n -> #3 update_output_div() \n")

    # Print Debug:
    print("\n #13 printing value:")
    print(radio_item_id)
    #// print(State(component_id('radioitem_12_4')))
    #// print(list_x5,"\n")

if __name__ == '__main__':
    app.run_server(debug=True)
