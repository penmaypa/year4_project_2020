import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("dub_rent.csv")
max_rows = 10
# print(df)

# df = dataframe

def find_missing_value(df):
    row = len(df)
    col = len(df.columns)
    missing_value = []

    count_row = 0
    while(count_row < row):
        #print("row ", count_row)
        count_col = 0
        while (count_col < col):
            is_empty = pd.isnull(df.iloc[count_row][count_col])
            if is_empty == True:
                print(count_row, ", ", count_col)

            count_col = count_col + 1

        count_row = count_row + 1

def find_missing_value_enable(enable, df):
    if enable == True:
        find_missing_value(df)


find_missing_value_enable(True,df)

def test_run():
    # print(len(df.columns))
    print(df.size)

print("================= \n")

# print(df.iloc[0:0])
# print(df.columns)
# print(df.iloc[0][0])
# print(df.iloc[2][0:-1])

print(pd.isnull(df.iloc[2][2]))


# print(len(df))
# print(df.size)
