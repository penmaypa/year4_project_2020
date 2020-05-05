import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("dub_rent.csv")
max_rows = 10
# print(df)

print("================= \n")

# print(df.iloc[0:0])
# print(df.columns)
# print(df.iloc[0][0])
# print(df.iloc[2][0:-1])

"""
with open('dub_rent.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)
"""

print(pd.isnull(df))
