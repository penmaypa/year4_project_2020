import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


def read_this_csv(csv_file):
    try:
        data_file = pd.read_csv(csv_file)
        data_valid = "valid"
        data_pack = (data_file, data_valid)
        return  data_pack
    except:
        data_file = pd.read_csv("DataException/exc.csv")
        data_valid = "invalid"
        data_pack = (data_file, data_valid)
        return  data_pack

def generate_table(h_name, data_pack, max_rows=100):
    dataframe = data_pack[0]
    is_data_valid = data_pack[1]
    if is_data_valid == "valid":
        return html.Div(
            [
                html.H4(
                    children= h_name,
                    style={
                        'textAlign':'center',
                        'font-weight':'bold'
                    },
                ),
                html.Table(
                    # Header
                    [html.Tr([html.Th(col) for col in dataframe.columns])] +

                    # Body
                    [html.Tr([
                        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                    ]) for i in range(min(len(dataframe), max_rows))],
                )
            ],
            style={
                'height':'500px',
                'width':'48%',
                'float':'left',
                #'backgroundColor': 'blue',
                'overflow' :'scroll'
            }
        )
    else:
        return html.Div(
            [
                html.H1(children='Error: No Valid Data',
                    style={
                        'textAlign':'center',
                        'font-weight':'bold',
                        'font-size':'20px'
                    }
                )
            ]
        )
