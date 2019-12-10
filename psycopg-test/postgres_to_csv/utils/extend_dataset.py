import pandas as pd

df = pd.read_csv('data.csv')

columns = df.columns
for column in columns:
    df[column+'_'] = df[column]
    df[column+'__'] = df[column]

df.columns = [column.replace(' ', '') for column in df.columns]
df.to_csv('new_data.csv', index=False)
