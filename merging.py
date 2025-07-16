#Merging in Pandas refers to the process of combining two or more DataFrame or named Series objects based on common columns or indices, similar to join operations in relational databases.

import pandas as pd 

sales_in_2023 =pd.DataFrame({
    "UserName": ["John", "Wick", "Vicky", "Ben", "Pat", "Mortal"],
    "UserId": [101, 102, 103, 104, 105, 106]
})

sales_in_2024 = pd.DataFrame({
    "UserId": [101,201,301,401,105,106],
    "sellItem": ["Bat", "Football", "Rackets", "Net", "Mobile", "Laptops"]
})

#merged_Both = pd.merge(sales_in_2023, sales_in_2024, on="UserId" ,how="inner")
#merged_Both = pd.merge(sales_in_2023, sales_in_2024, on="UserId" ,how="outer")
#merged_Both = pd.merge(sales_in_2023, sales_in_2024, on="UserId" ,how="left")
#merged_Both = pd.merge(sales_in_2023, sales_in_2024, on="UserId" ,how="right")
merged_Both = pd.merge(sales_in_2023, sales_in_2024,how="cross")
print("Merged Ok")
print(merged_Both)


'''
how: Specifies the type of merge (join), similar to SQL joins:

'inner' (default): Returns only rows where keys match in both DataFrames.
'outer': Returns all rows from both DataFrames, filling missing values with NaN where no match exists.
'left': Returns all rows from the left DataFrame and matching rows from the right. 
'right': Returns all rows from the right DataFrame and matching rows from the left. 
'cross': Creates a Cartesian product of the two DataFrames.
'''