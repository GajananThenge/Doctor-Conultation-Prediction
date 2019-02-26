src_dir=r"D:\Analytics Vidya\Final Participant Data Folder"
import pandas as pd
import seaborn as sns



train_df = pd.read_excel(r"D:\Analytics Vidya\Final Participant Data Folder\Final_Train.xlsx")


train_df= train_df[["Rating",'Experience',"Place"	,"Profile","Fees"]]

#Cheking Missing values
train_df.isnull().sum()

#Convert Age
train_df['Experience']=train_df['Experience'].str.replace(' years experience', '', regex=False)
train_df['Experience']=train_df['Experience'].astype(int)


#Check levels of categorical variables
train_df.dtype

train_df_wid_dummies = pd.get_dummies(train_df,drop_first=True)
#Create Model
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectFromModel



X_train = train_df_wid_dummies.iloc[:,:-1].copy()
y_train=train_df_wid_dummies.iloc[:,-1].copy()
model = RandomForestRegressor(n_estimators = 1000)

sel = SelectFromModel(RandomForestRegressor(n_estimators = 100))
model_fit=model.fit(X_train, y_train)
model.score(X_train, y_train)

