import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn import datasets

iris = datasets.load_iris()
#print(scale(iris.data))

model=DBSCAN(eps=0.5,min_samples=3)
model=model.fit(scale(iris.data))

print(model.labels_) # -1 for noise

from sklearn import metrics
sil = metrics.silhouette_score(iris.data, model.labels_)
print("silhouette = %f", sil) 

iris.data=iris.data[model.labels_!=-1]
iris.target=iris.target[model.labels_!=-1]


