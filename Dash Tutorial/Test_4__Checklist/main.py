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

def extractor(obj_missing_value):
    m.dprint("-> ... extractor()")
    list_of_rows = obj_missing_value[1]
    n_row = 0
    print("\n Printing row START: \n")
    print(list_of_rows)
    print("\n Printing row END: \n")

    for k in list_of_rows:
        listOf_cell = list_of_rows[n_row]
        # print("\n -> extractor() --> for k in list_of_rows : ", n_row ,"\n")
        # print("\n -> extractor() --> for k in list_of_rows --> printing this_cell ", this_cell ,"\n")

        print("\n -> extractor()"
            " \n --> for k in list_of_rows"
        )
        # n_cell = 0
        for this_cell in listOf_cell:

            print("\n -> extractor()",
                " \n --> for k in list_of_rows"
                "\n --> for this_cell in  listOf_cell"
                 ,this_cell ,"\n"
            )

            if this_cell[1] == False:
                m.dprint("-> for k in list_of_rows --> if this cell")
                bg_cell = "rgb(255, 179, 153)"

        n_row = n_row + 1

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

extractor(df_obj)

app.layout = html.Div([
    dcleanse_table(df)
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
