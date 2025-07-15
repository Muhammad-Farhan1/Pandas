import pandas as pd 
user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, None, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "London", "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, None, 80]
}
df = pd.DataFrame(user_info)

#by default value
#df.fillna(1, inplace=True)

#Filling missed value with some calculations of mean value:
df["ages"] = df["ages"].fillna(df["ages"].mean())
df["scores"] = df["scores"].fillna(df["scores"].mean())
print("Mean Values")
print(df)
