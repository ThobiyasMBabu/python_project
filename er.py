import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
d=pd.read_csv("E:/Thobi/Downloads/archive (1)/netflix_titles.csv")
print(d)
print(d.isnull().sum())
data=pd.DataFrame(d)
print(data)
d['director']=d['director'].fillna(d['director'].mode()[0])
d['cast']=d['cast'].fillna(d['cast'].mode()[0])
d['country']=d['country'].fillna(d['country'].mode()[0])
d['rating']=d['rating'].fillna(d['rating'].mode()[0])
d['duration']=d['duration'].fillna(d['duration'].mode()[0])
d['date_added']=d['date_added'].fillna(d['date_added'].mode()[0])
print(d.isnull().sum())
sns.countplot(data=d,x='type')
plt.title('count')
plt.xlabel('type')
plt.ylabel('release_year')
plt.show()
sns.scatterplot(data=d,x='duration',y='release_year',hue='type')
plt.title('scatterplot')
plt.xlabel('type')
plt.ylabel('release_year')
plt.show()



 
