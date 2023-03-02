## Reading data

import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.head(5))

print("----------------------------------")
print(df.tail(3))

print("----------------------------------")
print(df.columns)

print("----------------------------------")
print(df['Name'][0:4])

print("----------------------------------")
print(df.Name[0:4])

print("----------------------------------")
print(df[['Name','Type 1','Type 2']][0:4])

print("----------------------------------")
print(df.iloc[1])       #returns the raw where index is 1

print("----------------------------------")
print(df.iloc[1:5])

print("----------------------------------")
print(df.iloc[1,2])     #returns exact location

print("----------------------------------")

for index, row in df.iterrows():                #index = row index      #row = data series of each row
        print(index, row[['Name','Type 1']])

print("----------------------------------")
print(df.loc[df['Type 1'] == "Fire"])


