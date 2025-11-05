import  pandas as pd
import numpy as np
from sklearn.preprocessing import  StandardScaler
standard  = StandardScaler()
from sklearn.preprocessing import  MinMaxScaler
normalized = MinMaxScaler()
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
df= pd.read_csv(r"heart_disease_data.csv")
#print(df)

#print(df.head )
#print(df.describe())
#print(df.info())
#print(df.shape)
#print(df.values)
#print(df.index)
#print(df.columns)

#print(df.head())

sorted_df = df.sort_index(ascending=False)

#print(sorted_df)
individual = df['chol']
#print( individual.head())

# subsettting
inde = df['chol'] < 200
#print(inde)

kpa = df[df['chol'] < 200]
#print(kpa)



# Filter for rows where region is "Mountain"
#mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# Display the filtered DataFrame
#print(mountain_reg)

were_gender_1 = df[df['sex'] == 1 ]
#print(were_gender_1)

#print(df.head())
# compare 2 or call 2
sort_for_sex_n_age = df[(df['age'] > 40) & (df['sex'] == 1)]
#print(sort_for_sex_n_age)

# creating new column in the the table
#df['age1']= df['age'] + 1
#print(df)


# sorting
sort_df = df.sort_values('chol', ascending=False)
print(sort_df)

# sorting by multiply column
multi = df.sort_values(['chol','sex'], ascending=[True,False])

print(multi)

onwc = df[df['chol'] > 100].sort_values('chol',  )
print(onwc)

df.drop_duplicates(subset='chol', inplace=True )
print(df.info())
game = df.value_counts('chol')
print(game)
