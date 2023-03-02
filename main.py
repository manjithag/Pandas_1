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