import  pandas as pd

df= pd.read_csv(r"heart_disease_data.csv")
print(df)

print(df.info())
print(df.isnull().sum())