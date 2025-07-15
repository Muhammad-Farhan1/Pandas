import pandas as pd 
user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, None, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", None, "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, None, 80]
}
df = pd.DataFrame(user_info)
print(df)

print(df.dropna())

#This is not the recommded way because it can be the casue of data loss!
#Instead of doing this use fillna(value) method to fill some value for the placement of missing values