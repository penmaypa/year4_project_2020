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
print("\n printing data: \n", df)

print("\n #1 Selected data: \n")
print(df.iloc[0][0])
#print(df.rows)
#print("\n ")
##===========================

print("\n About to drop column...")
df = df.drop([1,3,5],axis=0)
#df = df.drop([1,3,5],)
#df.drop([1,3,5], axis=0, inplace=True)

print("\n The new data: \n", df)

print("\n > df.iloc[1,0] \n", df.iloc[1,])

print("\nAbout to reindex..")
# df = df.reindex(df,axis=1)
#df2 = df.reindex(df,axis=1)
df = df.reset_index(drop=True)

print(
    "\n #4 re-index df\n",
    df,
    "\n df 2\n",
    #df2
)
print("\n Deleting the second one...\n")
#df = df.drop(df.iloc[1,0])
print("\n #2 New data \n", df)
