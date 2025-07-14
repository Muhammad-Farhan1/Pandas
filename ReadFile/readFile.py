import pandas as pd

#Read CSV(Comma Separated Value) Files
read_data = pd.read_csv("ReadFile\data.csv")
#print(read_data.to_string())

# Read JSON
#JSON is plain text, but has the format of an object
json_data = pd.read_json("ReadFile\data.json")
print(json_data.to_string()) 

'''
If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
Tip: use to_string() to print the entire DataFrame.
JSON objects have the same format as Python dictionaries.
'''
