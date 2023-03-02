import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.head(5))

print("----------------------------------")

print(df.tail(3))