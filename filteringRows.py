import pandas as pd

user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, 22, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Multan", "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, 95, 80]
}
#DataFrame: A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

data = pd.DataFrame(user_info)
print(data)
# Boolean Indexing:

#Single Condition
filter_row = data[data["ages"] > 25]
#print("People with ages greater than 45")
#print(filter_row)

#Multiple Condition:
filter_data = data[(data["ages"] < 30) & (data["scores"] > 85)]
#print("Peope with age less than 25 and Scores greater than 80:")
#print(filter_data)


#Using 'loc' and 'iloc':

#loc (label-based indexing): Used to select rows based on their index labels or a boolean array.
using_loc = data.loc[data['cities'] == 'Lahore']
#print("Lahore City:")
#print(using_loc)

#iloc (integer-location based indexing): Used to select rows based on their integer positions.
using_iloc = data.iloc[:3]
#print("Row from 1 to 3")
#print(using_iloc)