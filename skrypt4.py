import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import linear_model, preprocessing
from sklearn.metrics import mean_squared_error
from scipy import stats

# PKT 1
# Choose five numerical columns
data = pd.read_csv('survey_results_public.csv',
    usecols=['WorkWeekHrs', 'YearsCode', 'Age1stCode',
    'CompTotal', 'ConvertedComp', 'CodeRevHrs', 'Hobbyist', 'Employment'])

# Search for depedency of variables using corr() function
data.corr()
# take a look at data
data.describe()

# Chosen (dependent value) y = CompTotal and (independent values) x = [ ConvertedComp, CodeRevHrs ]

#PKT 2

# replace values to be only numerical
data.replace(to_replace={'Yes': '1', 'No': '0'}, inplace=True)

# using one-hot encoding metod
one_hot_encoding = pd.get_dummies(data['Employment'])
data = data.drop('Employment', axis = 1)
data = data.join(one_hot_encoding)

# PKT 3

# Delete utliers using quantiles from ConvertedComp column
new_data1 = data[ (data['ConvertedComp'] >= data['ConvertedComp'].quantile(.15))
    & (data['ConvertedComp'] <= data['ConvertedComp'].quantile(.85))]

# Delete outliers using std from CodeRevHrs column
mean = np.mean(new_data1['CodeRevHrs'])
sd = np.std(new_data1['CodeRevHrs'])

# Delete utliers using quantiles from CodeRevHrs column
new_data2 = new_data1[ (new_data1['CodeRevHrs'] > mean - 3 * sd)
    & (new_data1['CodeRevHrs'] < mean + 3 * sd)]

new_data3 = new_data2[ (new_data2['CompTotal'] >= new_data2['CompTotal'].quantile(.15))
    & (new_data2['CompTotal'] <= new_data2['CompTotal'].quantile(.85))]


data_m = data[data['CompTotal'] < 120000]
x = data_m['CompTotal']

# Plots
plt.hist(x, bins=100)
plt.show();

data.plot()
plt.show()
new_data1.plot()
plt.show()
new_data2.plot()
plt.show()
new_data3.plot()
plt.show()

sns.boxplot(y='CompTotal', data=data)
plt.show();
sns.boxplot(y='CompTotal', data=new_data1)
plt.show();
sns.boxplot(y='CompTotal', data=new_data2)
plt.show();
sns.boxplot(y='CompTotal', data=new_data3)
plt.show();
sns.boxplot(y='CompTotal', data=data_m)
plt.show();

sns.violinplot(y='ConvertedComp', data=new_data3)
plt.show();

sns.regplot(y=new_data3['CompTotal'], x=new_data3['ConvertedComp'])
plt.show();

sns.jointplot(x='ConvertedComp', y='CompTotal', data=new_data3, kind='reg')
plt.show();

sns.jointplot(x='CodeRevHrs', y='CompTotal', data=new_data3, kind='reg')
plt.show();

sns.boxplot(y='CompTotal', x='ConvertedComp', data=new_data3)
plt.show();
sns.boxplot(y='CompTotal', x='ConvertedComp', data=data)
plt.show();

# PKT 4
#Linear regresion model and mean squared error

regr = linear_model.LinearRegression()
regr.fit(new_data3[['ConvertedComp']], new_data3[['CompTotal']])
# print(regr.predict([[60000]]))
# print(regr.predict([[100000]]))
# print(regr.predict([[240000]]))
mse = np.mean((regr.predict(new_data3[['ConvertedComp']]) - new_data3[['CompTotal']]) ** 2)

regr = linear_model.LinearRegression()
regr.fit(new_data3[['ConvertedComp', 'CodeRevHrs']], new_data3[['CompTotal']])
# print(regr.coef_)
# print(regr.predict(new_data3[['ConvertedComp', 'CodeRevHrs']]))
mse = np.mean((regr.predict(new_data3[['ConvertedComp', 'CodeRevHrs']]) - new_data3[['CompTotal']]) ** 2)

regr = linear_model.LinearRegression()
regr.fit(new_data3[['ConvertedComp', 'CodeRevHrs', 'Hobbyist']], new_data3[['CompTotal']])
# print(regr.coef_)
# print(regr.predict(new_data3[['ConvertedComp', 'CodeRevHrs', 'Hobbyist']]))
mse = np.mean((regr.predict(new_data3[['ConvertedComp', 'CodeRevHrs', 'Hobbyist']]) - new_data3[['CompTotal']]) ** 2)
