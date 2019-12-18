import visual_rep_mod
import pandas as pd
import dash

df = pd.read_csv("Data/emp2017.csv")
indexes = df.index

print(indexes)

#print(df.iloc[0:-1,0])
#print(df.iloc[0:-1,1])

sectors = (df.iloc[0:-1,0])
emp = (df.iloc[0:-1,1])


sec_list = []
emp_list = []
sec_emp =[]
for item in sectors:
    sec_list.append(item)
sx=0
for item in emp:
    s = sec_list[sx]
    sec_emp.append((s,item))
    sx = sx+1

print(sec_emp)


#print(sec_list)
