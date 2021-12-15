from xgboost import XGBRegressor
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv('tips.csv')
data.sex = data.sex.replace('Male','0')
data.sex = data.sex.replace('Female','1')
data.smoker = data.smoker.replace('No','0')
data.smoker = data.smoker.replace('Yes','1')
data.time = data.time.replace('Dinner','1')
data.time = data.time.replace('Lunch','0')
data.day = data.day.replace('Thur','0')
data.day = data.day.replace('Fri','1')
data.day = data.day.replace('Sat','2')
data.day = data.day.replace('Sun','3')
data.sex = data.sex.astype('int')
data.smoker = data.smoker.astype('int')
data.day = data.day.astype('int')
data.time = data.time.astype('int')
X = data.drop('tip',axis=1)
y = data['tip']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=22)
xg = XGBRegressor(learning_rate=0.1)
xg.fit(X_train,y_train)
lg = LinearRegression()
lg.fit(X_train,y_train)
model = pickle.dump(xg,open('model.pkl','wb'))
logis = pickle.dump(lg,open('logis.pkl','wb'))

model_ = pickle.load(open('model.pkl','rb'))
a = np.array([10.34,0,0,3,1,3])
aa = a.reshape(1,6)
print(model_.predict(aa))
print(aa)