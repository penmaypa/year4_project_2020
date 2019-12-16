import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go


def generate_table(dataframe, max_rows=100):
    if is_data_valid == True:
        return html.Table(
            # Header
            [html.Tr([html.Th(col) for col in dataframe.columns])] +

            # Body
            [html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))],
            style={
                

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
