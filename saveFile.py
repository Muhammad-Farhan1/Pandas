import pandas as pd
intro = {
    "Name":["Bob" , "John", "Denish" ],
    "Age": [17,45,23],
    "Country": ["Pakistan", "India", "Australia"]
}

data = pd.DataFrame(intro)
print(data)

#data.to_csv("Output.csv" , index=False) save the csv file  
#data.to_excel("OutPut.xlsx" , index=False) save the excel file  
#data.to_json("Output.json", index=False) save the json file  