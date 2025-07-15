#The insert() method in Pandas is used to add a new column to a DataFrame at a specified positionThe insert() method in Pandas is used to add a new column to a DataFrame at a specified position
#DataFrame.insert(loc, column, value, allow_duplicates=False)

import pandas as pd

user_info = {
    "names": ["Ali", "Sara", "John", "Fatima", "Omar", "Ayesha", "David", "Zara"],
    "ages": [25, 30, 22, 28, 35, 27, 24, 29],
    "cities": ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Multan", "Peshawar", "Quetta", "Faisalabad"],
    "scores": [88, 92, 75, 85, 90, 78, 95, 80]
}

data = pd.DataFrame(user_info)
print(data)

#adding a new column and its data:

data.insert(0 , "User_Id" , [401, 402, 403, 404, 405, 406, 407, 408])
print("New Data")
print(data)
