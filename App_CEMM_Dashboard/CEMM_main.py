import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import visual_rep_mod as visual

data_directory_file = "Data/emp2017.csv"
visual.is_data_valid = True

try:
    df = pd.read_csv(data_directory_file)
except:
    visual.data_is_data_valid = False
    print("\n EXCEPTION:  Data file not found \n")
    df = pd.read_csv("DataException/exc.csv")

def generate_visuals():
    table_1 = visual.generate_table(df)
    table_2 = visual.generate_table(df)



def generate_pieChart(labels, values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    return fig.show()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
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
            )
        ],
        style={
            'backgroundColor':'rgb(112, 180, 255, 0.5)'
        }
    ),

    html.H4(children='Employment by Sector (2017)'),

    visual.generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
