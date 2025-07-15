import pandas as pd
user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, 22, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Multan", "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, 95, 80]
}

data = pd.DataFrame(user_info)
#print(data)

#Deleting single columns:
data.drop(columns="cities", inplace=True)
print(data)

#Deleting multiple columns:
data.drop(columns=["scores","ages"] , inplace=True)
print(data)

#inplace: If True, the operation modifies the original DataFrame directly and returns None. If False (default), it returns a new DataFrame with the specified columns removed, leaving the original DataFrame unchanged.