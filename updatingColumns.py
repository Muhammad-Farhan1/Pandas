import pandas as pd

user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, 22, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Multan", "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, 95, 80]
}

data = pd.DataFrame(user_info)
print(data)

#Updating single value:
data.loc[0, "scores"] = 90
#print(data)

#Updating Mutliple values:
data["scores"] = data["scores"] - 2
print(data)