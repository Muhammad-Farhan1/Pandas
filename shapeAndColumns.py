import pandas as pd

user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, 22, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Multan", "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, 95, 80]
}
#DataFrame: (cover whole dataset)
data = pd.DataFrame(user_info)
print(data)

#Shape of a DataFrame:
#The shape attribute of a pandas DataFrame returns a tuple representing its dimensionality.
#The first element of the tuple is the number of rows, and the second element is the number of columns.
print(f"Shape is : {data.shape}")

#You can get the number of rows specifically with df.shape[0] and the number of columns with df.shape[1]
print(f"Shape is : {data.shape[0]}") #It would print rows
print(f"Shape is : {data.shape[1]}") #It would print columns

#Columns in a DataFrame:
#You can access the column names using df.columns.
print(data.columns)

#You can select specific columns by providing a list of column names within square brackets: df[['Column1', 'Column2']].
print(data[['names', 'cities']])