import  pandas as pd
import  numpy as np
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.linear_model import  LogisticRegression
from sklearn.model_selection import train_test_split



df = pd.read_csv(r"heart_disease_data.csv")
print(df.head())
print(df.info()) # give infor about the table
print(df.describe()) # give a stasitical analysis for the table
print(df.shape) # check for number of row and columns
print(df.isnull().sum()) # give the sum for missing values in the columns
print(df.columns)


#check for the distribution of the target variable
print(df.value_counts(['target']))

# we then split the date to x = feature variable and y = target variable

x = df.drop('target',axis=1)
y = df['target']

print(x.head())
print(y.head())

# split the date into train and test data set

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, stratify=y, random_state=42)

# train the model using the x_train and y_train

model = LogisticRegression()
model.fit(x_train,y_train)

# make predictions using x_text
y_pred = model.predict(x_test)

#evaluate model accuracy confusion matric, classification report, accuracy score

#accuracy score
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy score: {accuracy * 100:.2f}%")

# classification report
print(classification_report(y_test,y_pred))

print(confusion_matrix(y_test,y_pred))