import visual_rep_mod
import pandas as pd
import dash

df = pd.read_csv("Data/emp2017.csv")
indexes = df.index


print(df.iloc[0:-1,0])
print(df.iloc[0:-1,1])
