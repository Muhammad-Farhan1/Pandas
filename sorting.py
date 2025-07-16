#--------Syntax--------
#dataframe.sort_values(by, axis, ascending, inplace, kind, na_position, ignore_index, key)

import pandas as pd

students = {
    "father_name": ["Robert", "Michael", "David", "Richard", "James"],
    "roll_number": [101, 102, 103, 104, 105],
    "name": ["Bob","Alice", "Diana", "Ethan", "Charlie"],
    "age": [18, 17, 14, 18, 17],
}
df = pd.DataFrame(students)
#Single Column
#df.sort_values(by="name", ascending=True, inplace=True)

#Multiple Columns:
df.sort_values(by=["father_name","age"], ascending=True , inplace=True)
print("Sorted Value")
print(df)