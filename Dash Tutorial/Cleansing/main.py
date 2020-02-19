import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("dub_rent.csv")
max_rows = 10
# print(df)

#===========================
"""
--------------------------------
FUNCTION:
    obj_list_of_missing_values
---------------------------------
 INPUT:  dataframe
 OUTOUT: tuple -> layered with tuple and lists

 ACCESSING THE OBJECT:
    Tuple (dataframe, Lists[])
        ^ dataframe
        ^ Lists: L1 - list of rows
            ^ List: L2 - New Row: Contains a list of cells of thes same row
                ^ Tupple (row_number, Boolean, Value ):
                    > Row number
                    > Boolean: If the value of the cell is valid
                    > Value: The value of the cell
"""
def obj_list_of_missing_values(df):
    row = len(df)
    col = len(df.columns)

    final_obj_pack =()
    l1_list = []
    l2_list = [] # new row
    l3_tup = ((0,0),True, 'value')
    is_valid_value = True


    count_row = 0
    print("\n -> while(count_row < row) -> ... \n")
    while(count_row < row):
        new_row = []
        is_valid_row = True
        #row_empty_exist = False

        count_col = 0
        print("\n -> while(count_row < row) -> while (count_col < col) \n")
        while (count_col < col):
            is_valid_value=True

            if pd.isnull(df.iloc[count_row][count_col]) ==  True:
                is_valid_value = False
                is_valid_row = False

            if is_valid_value == False:
                new_row.append(((row,col),False, df.iloc[count_row][count_col]))
            else:
                new_row.append(((row,col),True, df.iloc[count_row][count_col]))

            count_col = count_col + 1

        if is_valid_row == False:
            l1_list.append(new_row)

        count_row = count_row + 1
    # print("\n"," -> Printing output: List > List > Tuple ")
    # print(l1_list)
    final_obj_pack = (df,l1_list)
    output_list_of_missing_values = final_obj_pack

    return output_list_of_missing_values

#========================================

#=========================================
# INPUTS:  df = dataframe
# OUTPUTS:  A LIST of rows that has missing values

def find_missing_value(df):
    row = len(df)
    col = len(df.columns)

    l1_list = []
    l2_list = []
    l3_tup = {True, 'value'}


    count_row = 0
    while(count_row < row):
        #print("row ", count_row)
        new_row = []
        row_empty_exist = False

        count_col = 0
        while (count_col < col):
            is_empty = pd.isnull(df.iloc[count_row][count_col])

            if is_empty == True:
                #print(count_row, ", ", count_col)
                new_row.append("**", df.iloc[count_row][count_col],"**")
            else:
                new_row.append(df.iloc[count_row][count_col])

            count_col = count_col + 1

        if row_empty_exist == True:
            missing_value.append(new_row)

        count_row = count_row + 1

    print(missing_value)

"""
def find_missing_value_enable(false, df):
    if enable == True:
        find_missing_value(df)
"""


# find_missing_value_enable(True,df)

def test_run():
    # print(len(df.columns))
    print(df.size)

print("================= \n")
print(obj_list_of_missing_values(df))

# print(df.iloc[0:0])
# print(df.columns)
# print(df.iloc[0][0])
# print(df.iloc[2][0:-1])

#print(pd.isnull(df.iloc[2][2]))


# print(len(df))
# print(df.size)
