import dash
import csv
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from cemm_lib import visual_rep_mod as visual
from cemm_lib import misc_mod as m
from cemm_lib import data_cleansing as cleansing


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("dub_rent.csv")

print("\n #1")
print(df.iloc[2][0])
#print(df.rows)
#print("\n ")
##===========================
