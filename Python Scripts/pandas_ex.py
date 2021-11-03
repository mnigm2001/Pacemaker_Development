import pandas as pd
import itertools


df = pd.read_csv("test.csv")

df['values'] = ""

for i in range(len(df)):
    df['values'][i] = list([*range(df["Lower Limit"][i], df["Upper Limit"][i], df['Increment'][i])])

df = df.groupby(['Parameter']).agg(list)

for i in range(len(df)):
    df['values'][i] = list(itertools.chain(*df['values'][i]))


## this is for creating lists from a csv value 
## basically, if you enter 1,2,3,4,5 into one cell in the csv, this will create a list from that
'''cols = ['Not Pattern', 'Lower Limit', 'Upper Limit', 'Increment']

for col in cols:
    for i in range(len(df[col])):
        if pd.notnull(df[col][i]):
            if df[col][i].find(",") != - 1:
                df[col][i] = list(df[col][i].split(","))

##df['values'] = list([*range(df["Lower Limit"], df["Upper Limit"], df['Increment'])])

##df['values'] = df["Lower Limit"] '''


                