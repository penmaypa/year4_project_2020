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
