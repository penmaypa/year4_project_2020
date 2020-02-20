import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from cemm_lib import visual_rep_mod as visual
from cemm_lib import misc_mod as m
from cemm_lib import data_cleansing as cleansing


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("dub_rent_missing.csv")
df_obj = cleansing.obj_list_of_missing_values(df)

#===========================

def extractor__to_html_row(obj_missing_value):
    this_df = obj_missing_value[0]
    m.dprint("-> ... extractor()")
    list_of_rows = obj_missing_value[1]
    n_row = 0
    list_of_row_radio_items = []


    for k in list_of_rows:
        listOf_cell = list_of_rows[n_row]
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

            list_of_row_radio_items.append(
                html.Tr(
                    [
                        html.Td(
                            cell_value,
                            style={
                                'backgroundColor' : bg_cell
                            }
                        )

                    ]
                    +
                    [
                        dcc.RadioItems(
                            id = 'radioitems_'+str(cell_index_x)+'_'+str(cell_index_y),
                            options=[
                                 {'label': 'Ignore', 'value': 'ign'},
                                 {'label': 'Delete', 'value': 'del'}
                            ],
                        )
                    ]
                )
            )

        n_row = n_row + 1

    html_table =html.Table(
                list_of_row_radio_items
            )

    print("\n printing the object: \n")
    print(obj_missing_value)
    print("\n printing the return: \n")
    print(html_table)

    return html_table

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
                            value='ign'
                        ),
                    ],
                ) for i in range(len(dataframe))
            ],
        )
    )



#===================================

# extractor(df_obj)
app.layout = html.Div([
    # dcleanse_table(df)
    extractor__to_html_row(df_obj)
    # visual.generate_table_v2(df_obj[0])
])

"""
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)
"""
def set_cities_value(available_options):
    return available_options[0]['value']

if __name__ == '__main__':
    app.run_server(debug=True)
