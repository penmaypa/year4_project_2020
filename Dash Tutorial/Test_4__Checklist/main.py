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
list_of_radio_items_id = []


#===========================

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
                id = 'radioitem_'+str(cell_index_x)+'_'+str(cell_index_y),
                options=[
                     {'label': 'Ignore', 'value': 'ign'},
                     {'label': 'Delete', 'value': 'del'}
                ],
                value='ign',
                labelStyle={'display': 'inline-block'}
            ),
            #// add_to_bt_itemlist(component_id, component_value)
            print("\n #16 \n"),
            list_of_radio_items_id.append('radioitem_'+str(cell_index_x)+'_'+str(cell_index_y))
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
    #   Table -- with rows of missing value + option buttons
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
    print(obj_missing_value)
    print("\n printing the return: \n")
    print(html_table)
    print("\n")

    return html_output

#======================

def dcleanse_table(df):
    dataframe = df
    start_n = 0

    #rows_with_missing_value = dcc.

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

def callback_loop_radioitem_id():
    list_of_rd_input=[]
    for item in list_of_radio_items_id :
        list_of_rd_input.append(State(item,'value'))

    print("\n #18 ",list_of_rd_input,"\n")
    return list_of_rd_input
#===================================

# extractor(df_obj)
app.layout = html.Div([
     # dcleanse_table(df)
    extractor__to_html_row(df_obj),
    # visual.generate_table_v2(df_obj[0])
   html.Div(
        id='output-container-button',
        children="output here"
   ),

   print("\n #17 ", list_of_radio_items_id,"\n")
   #// itemx_state = State('radioitem_12_4','value'),

  #// print("\n #12 Printing state :\n", itemx_state)
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
    return

if __name__ == '__main__':
    app.run_server(debug=True)
