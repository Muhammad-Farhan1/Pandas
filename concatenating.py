import pandas as pd 

sales_in_2023 =pd.DataFrame({
    "UserName": ["John", "Wick", "Vicky"],
    "UserId": [101, 102, 103]
})

sales_in_2024 = pd.DataFrame({
    "UserName": ["Ben", "Ronaldo", "Ricky"],
    "UserId": [101,201,301]
})

joining = pd.concat([sales_in_2023, sales_in_2024], axis=1, ignore_index= True)
#axis=0 -> Vertically and axis=1 -> Horizontally
print(joining)