import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn import datasets
from sklearn import metrics

iris = datasets.load_iris()
print(scale(iris.data))

model=KMeans(n_clusters=3)
model=model.fit(iris.data)

labels = model.labels_
sil = metrics.silhouette_score(iris.data, labels)
print("silhouette = %f", sil) 
 

print(model.labels_)

plt.scatter(iris.data[:,0],iris.data[:,1],c=model.labels_.astype(np.float))
plt.show()

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


fig = pyplot.figure()
ax = Axes3D(fig)

X = iris.data[:,0]
Y = iris.data[:,1]
Z = iris.data[:,2]

LABEL_COLOR_MAP = {0 : 'r',
                   1 : 'k',
                   2 : 'b',
                   }
label_color = [LABEL_COLOR_MAP[l] for l in model.labels_]

ax.scatter(X, Y, Z, c=label_color)
pyplot.show()
