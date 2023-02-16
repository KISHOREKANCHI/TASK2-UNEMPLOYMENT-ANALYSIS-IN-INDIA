#Import the libraries
import numpy as np
import pandas as pd
import sklearn
import plotly
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
#from google.colab import drive



#Import the dataset
# drive.mount('/content/gdrive')
# india1=pd.read_csv('/content/gdrive/MyDrive/Unemployment in India.csv')
# india2=pd.read_csv('/content/gdrive/MyDrive/Unemployment_Rate_upto_11_2020.csv')
india1=pd.read_csv('Unemployment in India.csv')
india2=pd.read_csv('Unemployment_Rate_upto_11_2020.csv')



#Analysis
india1.dropna(inplace=True)
india1



india2.dropna(inplace=True)
india2



india1.info()
india2.info()



india1.describe
india2.describe



india1.columns=['region','date','frequency','unemployed','employed','labour','area']
india2.columns=['region','date','frequency','unemployed','employed','labour','direction','longitude','latitude']



#Checking null values
print(india1.isnull().sum())
print(india2.isnull().sum())



plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(12,10))
plt.title('Unemployment Rate in India')
sns.heatmap(india1.corr(), annot=True, cmap='coolwarm')
plt.show()
plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(12,10))
plt.title('Unemployment Rate in India')
sns.heatmap(india2.corr(), annot=True, cmap='coolwarm')
plt.show()



plt.figure(figsize=(20,15))
sns.histplot(x="employed",hue="region",data=india1)
plt.title("Employment Rate in India")
plt.show()
plt.figure(figsize=(15,15))
sns.histplot(x="employed",hue="region",data=india2)
plt.title("Employment Rate in India")
plt.show()


plt.figure(figsize=(20,15))
sns.histplot(x="unemployed",hue="region",data=india1)
plt.title("Unemployment Rate in India")
plt.show()
plt.figure(figsize=(20,15))
sns.histplot(x="unemployed",hue="region",data=india1)
plt.title("Unemployment Rate in India")
plt.show()



sns.pairplot(india1,height=4.5)
sns.pairplot(india2,height=4.5)



sns.pairplot(india1,height=4.9, hue="region")
sns.pairplot(india2,height=5, hue="direction")



india1.columns=['region','date','frequency','unemployed','employed','labour','area']
unemployment=india1.iloc[:,[0,3,6]].copy()
unemployment
figure=px.sunburst(unemployment,path=['area','region'],values='unemployed',width=700,height=700,title='Unemployment rate in India')
figure.show()
india2.columns=['region','date','frequency','unemployed','employed','labour','direction','longitude','latitude']
unemployment=india2.iloc[:,[0,3,6]].copy()
unemployment
figure=px.sunburst(unemployment,path=['direction','region'],values='unemployed',width=700,height=700,title='Unemployment rate in India')
figure.show()



india1.columns=['region','date','frequency','unemployed','employed','labour','area']
india2.columns=['region','date','frequency','unemployed','employed','labour','direction','longitude','latitude']
fig=plt.figure(figsize=(20,10))
ax=sns.lineplot(y="unemployed",x="region",data=india1)
ax1=sns.lineplot(y="unemployed",x="region",data=india2)
plt.xticks(rotation=40)
plt.show()