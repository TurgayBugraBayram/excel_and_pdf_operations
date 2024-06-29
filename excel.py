import pandas as pd

df = pd.read_excel('PA-Forms_Tool.xlsx', header=1)

columns = ['AK', 'IA', 'ID', 'IL', 'MI', 'MN', 'MT', 'ND', 'NV', 'OR', 'SD', 'UT', 'WA', 'WI']

count_dict_big_X = {}

for col in columns:
    count_dict_big_X[col] = df[col].value_counts().get('X', 0)

for col, count in count_dict_big_X.items():
    print(f"{col} sütununda {count} tane 'X' var.")
