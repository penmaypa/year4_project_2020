import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from cemm_lib import visual_rep_mod as visual


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("dub_rent.csv")

#===========================

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
