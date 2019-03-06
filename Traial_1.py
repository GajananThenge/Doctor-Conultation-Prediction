# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:42:24 2019

@author: gajanan.thenge
"""

import pandas as pd
import seaborn as sns



train_df = pd.read_excel(r"D:\Analytics Vidya\Final Participant Data Folder\Final_Train.xlsx")

#Exploratory data analysis
#Find top 10 costliest doctors in area

gb_area_profile = train_df.groupby(by=['Place'])['Fees'].mean()

gb_area_profile.plot.bar()








test_df = pd.read_excel(r"D:\Analytics Vidya\Final Participant Data Folder\Final_Test.xlsx")

train_last_row= train_df.shape[0]


dataset = pd.concat([train_df.iloc[:,:-1],test_df],sort=False)
dataset=dataset[["Qualification","Rating",'Experience',"Place","Profile"]]
dataset['Experience']=dataset['Experience'].str.replace(' years experience', '', regex=False)
dataset['Experience']=dataset['Experience'].astype(int)

replace_dataset = dataset.copy()
cat_dataset_cols= replace_dataset.select_dtypes('object').columns
result_dict ={}
for col in cat_dataset_cols:
    replace_dataset[col] = replace_dataset[col].astype('category')
    
    result_dict[col]=list(zip(replace_dataset[col].cat.codes, replace_dataset[col].cat.categories))
    replace_dataset[col]  = replace_dataset[col].cat.codes


#Separate out train and test dataset
X_train = replace_dataset.iloc[:train_last_row]
X_test = replace_dataset.iloc[train_last_row:]


#Output
y_train = train_df.iloc[:,-1]


#Model Training
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 1000)
model.fit(X_train,y_train)
model.score(X_train,y_train)

#Model Prediction
predcted = model.predict(X_test)

test_df['Fees'] = predcted


test_df.to_excel("First_atempt.xlsx",index=False)


