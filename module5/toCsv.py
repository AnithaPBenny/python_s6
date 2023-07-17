import pandas as pd
mydict = {
    'Name' : ['A','B'],
    'Country' : ['India','England']
}
df = pd.DataFrame(mydict)
df = pd.to_csv("myFile.csv")
print(df)