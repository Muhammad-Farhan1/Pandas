import pandas as pd

data_analyze = pd.read_json("ReadFile\data.json")
#Note: if the number of rows is not specified, the head() method will return the top 5 rows.
#Head Method:
print("Print first 5 rows:")
print(data_analyze.head())


#Tail Method:
#print("Print last 10 rows:")
#print(data_analyze.tail(10))

#Info Method (Info About the Data):
info_data = pd.read_csv("ReadFile/data.csv")
#print(info_data.info())


