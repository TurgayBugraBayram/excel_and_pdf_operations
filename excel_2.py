import pandas as pd

file_path = 'PA-Forms_Tool.xlsx'
df = pd.read_excel(file_path, header=1)

columns = ['AK', 'IA', 'ID', 'IL', 'MI', 'MN', 'MT', 'ND', 'NV', 'OR', 'SD', 'UT', 'WA', 'WI']

selected_state = input("Please enter a state name (e.g., 'AK'): ")

if selected_state not in columns:
    print("Invalid state name. Please enter a valid state name.")
else:
    count_X = df[selected_state].value_counts().get('X', 0) + df[selected_state].value_counts().get('x', 0)

    form_data_X = df.loc[df[selected_state].isin(['X', 'x']), ['Form number w/Edition date', 'Form Name']]

    print(f"There are {count_X} in the {selected_state} column.")

    if count_X > 0:
        print(count_X)
        print(form_data_X)


