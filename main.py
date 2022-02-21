from traceback import print_tb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
data = datasets.load_iris() 
#map like objects returning ['target', 'data', 'DESCR', 'feature_names']
#dataset['target'] - 1D numpy array of target attribute values
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target)
df.head()

#visualisasi hasil ConvexHull
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])           # axis point 
plt.ylabel(data.feature_names[1])           # ordinate
for i in range(len(data.target_names)):     # akan ada 3 convex hull karena target[0..2]
    bucket = df[df['Target'] == i]          # pembagian data berdasarkan target
    bucket = bucket.iloc[:,[0,1]].values    # return 2d array [[a,b]] from attribute Petal width and Petal length 
    hull = ConvexHull(bucket) #bagian ini diganti dengan hasil implementasi ConvexHull Divide & Conquer
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i]) 
    for simplex in hull.simplices:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i]) 
plt.legend()