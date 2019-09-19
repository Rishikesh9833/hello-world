import numpy as np
x = np.array([1,2,3])
y = np.linspace(2.0,3.0,num=3)
z = np.arange(12).reshape(2,6)
ru = np.random.random((2,6))
rn = np.random.normal(0,1,(6,4))
np.array([[[1,2,3]]])
s= np.array([[[1,2,3]]])
s1=s.T

#shape
x.shape,rn.shape
s.shape #(1,1,3)
s1.shape#(3,1,1)

#dim
x.ndim,rn.ndim
#access
x[0]
z[0,0]
z[:,0:2]
z[0:2,:]
z[z>2]
z[(z>2)&(z<4)]
z[0,0]=20
#oprations
x*x
x+y
x-y
np.log(x)
np.sin(y)
rn*2+3

#metrix
np.dot(ru,rn)

#sum
np.sum(z)#66
np.sum(z,axis=0)#array([ 6,  8, 10, 12, 14, 16]) Columwise
np.sum(z,axis=1)#array([15, 51]) Rowwise

#Sort

#insert

import pandas as pd
iris = pd.read_csv("data/iris.csv")
iris.columns
iris.index
iris.dtypes
iris.head()

#Access
iris.SepalLength
iris['SepalLength']
iris[['SepalLength','PetalLength']]
#number based
iris.iloc[0:10,0]
iris.iloc[0:10,[0,1]]

# Lable Based - Column and index
iris.loc[0:10,'SepalLength']
iris.loc[0:10,['SepalLength','PetalLength']]
iris.loc[iris.Name=='Iris-setosa',['SepalLength','PetalLength']]

#new Column
iris_m = iris.copy()
iris_m['SepalRatio']=iris_m.SepalWidth/iris_m.SepalLength
iris_m['PetalRatio']=iris_m.PetalWidth/iris_m.PetalLength
iris_m.head()
import matplotlib.pyplot as plt
iris_m.plot(kind='scatter',x='SepalRatio',y='PetalRatio')
plt.show()

#cluster center
features =[['SepalRatio'],['PetalRatio']]
from sklearn.cluster import *
kmeans = KMeans(n_clusters=2,random_state=0).fit(features)
kmeans.cluster_center_
kmeans.labels_

#write to csv
iris.groupby('Name').agg({'SepalLength':['min','max'],'PetalLength':'count'}).to_csv("processed.csv")
iris.groupby('Name').agg({'SepalLength':['min','max'],'PetalLength':'count'}).head()
                # PetalLength SepalLength
                      # count         min  max
# Name
# Iris-setosa              50         4.3  5.8
# Iris-versicolor          50         4.9  7.0
# Iris-virginica           50         4.9  7.9


lst =[1,2,3]
g = [e*e for e in lst]
g
g2 = (e*e for e in lst)
g2
list(g2)
i=iter(g2)
next(i)
next(i)
next(i)
g2 = (e*e for e in lst)
for e in g2:
    print(e)
    
    
def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

for e in fib():
    print(e)
    
i = iter(fib())
next(i)

import itertools
itertools.islice(i,10)
len(str(list(itertools.islice(i,2000))[0]))


# Exception
class MyException(Exception):
    pass
    
def f():
    raise Exception("Some Error")
    
try:
    f()
except Exception as ex:
    print(ex)
finally:
    print("always")



















