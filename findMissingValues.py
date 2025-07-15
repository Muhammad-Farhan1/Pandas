import pandas as pd 
user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, None, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", None, "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, None, 80]
}
df = pd.DataFrame(user_info)
print(df)

#isnull() returns a DataFrame of Boolean value where True represents missing data (NaN). 
print(df.isnull())

#The df.isnull().sum() method in Pandas is used to count the number of missing values (NaN or null values) in each column of a DataFrame.
print(df.isnull().sum())
