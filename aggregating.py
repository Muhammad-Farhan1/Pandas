#Aggregating values in Pandas involves applying functions to summarize data, typically for columns or groups within a DataFrame. 

import pandas as pd
students = {
    "marks": [401, 345, 455, 505, 296,343, 223, 543]
}
df = pd.DataFrame(students)
#sum_marks = df.agg("sum")
#mean_value = df.agg("mean")
#median_value = df.agg("median")
max_value = df.agg("max")
print(max_value)

'''
Pandas offers various built-in aggregation functions:
sum(): Computes the sum of values.
mean(): Calculates the average value.
median(): Determines the middle value.
min(): Finds the minimum value.
max(): Finds the maximum value.
count(): Counts the number of non-null values.
nunique(): Counts the number of unique values.
std(): Calculates the standard deviation.
var(): Computes the variance.
first(): Returns the first value in a group.
last(): Returns the last value in a group.
size(): Returns the size of each group.
describe(): Generates descriptive statistics (count, mean, std, min, max, percentiles).
'''
#Grouping 
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Sales': [100, 150, 120, 80, 200, 90],
    'Region': ['East', 'West', 'East', 'North', 'West', 'South']
}
data_frame = pd.DataFrame(data)

# Group by 'Category' and calculate the sum of 'Sales'
grouped_sales = data_frame.groupby('Category')['Sales'].sum()
print("Sum of Sales by Category:\n", grouped_sales)

# Group by 'Category' and 'Region' and calculate the mean of 'Sales'
region = data_frame.groupby(['Category', 'Region'])['Sales'].mean()
print("\nMean of Sales by Category and Region:\n", region)