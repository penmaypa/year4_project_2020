import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

def read_csv_v2(this_file):
    df = this_file
    print(this_file)

def read_this_csv(csv_file):
    try:
        print("\n -> read_this_cv() -> try() \n")
        data_file = pd.read_csv(csv_file)
        data_valid = "valid"
        data_pack = (data_file, data_valid)
        return  data_pack, print("\n -> read_this_csv() -> return :... \n"), print(data_file)
    except:
        print("\n -> read_this_cv() -> exception() \n")
        data_file = pd.read_csv("DataException/exc.csv")
        data_valid = "invalid"
        data_pack = (data_file, data_valid)
        return  data_pack

def generate_table(h_name, data_pack, max_rows=100):
    dataframe = data_pack[0]
    is_data_valid = data_pack[1]
    print("\n -> genreate_table() \n")

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
                        'font-size':'20px',
                        'margin-top':'100px'
                    }
                )
            ],
            style={
                'height':'500px',
                'width':'48%',
                'float':'left',
                'overflow' :'scroll',
                'backgroundColor':'rgba(216, 222, 109, 0.3)',
            }
        )


def generate_table_v2(csv_file, max_rows=100):
    dataframe = csv_file
    print("\n -> genreate_table()_v2 \n")

    return html.Div(
        [
            html.H4(
                children= "Heading",
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

def generate_table_v3():
    dataframe = pd.read_csv("data/emp2017.csv")
    max_rows = 100
    print("\n -> genreate_table()_v3 \n")

    return html.Div(
        [
            html.H4(
                children= "Heading",
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

def generate_table_v4():

        dataframe = pd.read_csv("data/emp2017.csv")
        max_rows = 100
        print("\n -> genreate_table()_v3 \n")

        return html.Div(
            [
                html.H4(
                    children= "Heading",
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


def generate_barChart(h_name, data_pack):
    try:
        datafile = data_pack[0]
        is_data_valid = data_pack[1]

        col_0 = datafile.iloc[0:-1,0]
        col_1 = datafile.iloc[0:-1,1]

        col_0_list = []
        col_1_list = []

        for item in col_0:
            col_0_list.append(item)

        for item in col_1:
            col_1_list.append(item)

        return html.Div(
            [
                html.H1(
                    [
                        dcc.Graph(
                            id='Graph1',
                            #
                            figure={
                                'data': [
                                    {'x': col_0_list, 'y': col_1_list, 'type': 'bar', 'name': h_name},
                                ],
                                'layout': {
                                    'plot_bgcolor': 'white',
                                    'paper_bgcolor': 'F0F7BE',
                                    'font': {
                                        'color': 'black'
                                    },
                                }
                            }
                        )
                    ],
                    style={
                        'height':'500px',
                        'width':'48%',
                        'float':'right',
                        'overflow' :'scroll'
                    }
                )
            ]
        )
    except:
        return html.Div(
            [
                html.H1(children='Error: No Valid Data',
                    style={
                        'textAlign':'center',
                        'font-weight':'bold',
                        'font-size':'20px',
                        'margin-top':'100px',
                    }
                )
            ],
            style={
                'height':'500px',
                'width':'48%',
                'float':'right',
                'overflow' :'scroll',
                'backgroundColor':'rgba(216, 222, 109, 0.3)',
            }
        )
