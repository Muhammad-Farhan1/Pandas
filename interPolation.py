#Interpolation :Interpolation is a technique to estimate unknown values between known data points. Pandas provides several interpolation methods via the interpolate() function.
import pandas as pd
import numpy as np


data = {
    "time": [1, 2, 3, 4, 5],
    "value": [100, np.nan , 300 , np.nan, 500],
    "Prices": [254, 4000, np.nan, 8080, np.nan]
}
df = pd.DataFrame(data)
print("Before Interpolation")
print(df)

#Linear Method : 'linear': The default method, which treats values as equally spaced and performs linear interpolation.
df["value"] = df["value"].interpolate(method="linear" , axis=0)
df["Prices"] = df["Prices"].interpolate(method="linear" , axis=0)
print("After Interpolation")
print(df)


#Polynomial Interpolation
#Method: Fits a polynomial curve to the data points
#Best for: Non-linear data patterns
df["Prices"] = df["Prices"].interpolate(method="polynomial", order=2)
print("After interpolation method of polynomial")
print(df)


#TimeStamp Interpolation
time_data = {
    "values": [23, np.nan, 45, np.nan, 78],
    "timestamp": pd.to_datetime(['2023-01-01', '2023-01-03', 
                               '2023-01-06', '2023-01-10', '2023-01-15'])
}
df = pd.DataFrame(time_data)

# Set the timestamp column as the index
df = df.set_index('timestamp')  # This is the crucial step

print("Before Interpolation of Time")
print(df)

# Now perform time-based interpolation
df["values"] = df["values"].interpolate(method='time')
print("After Interpolation of time")
print(df)