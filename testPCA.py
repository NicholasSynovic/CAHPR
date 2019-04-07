print(__doc__)

import GetData
import numpy
import matplotlib.pyplot as plt

from numpy import array as arr
from sklearn import datasets
from sklearn.decomposition import PCA

gd = GetData.GetData(r"JSON\Crimes\crimes0.json")
raw = gd.build2DList(remove=4)
x = raw["DATA"]
y = raw["REMOVED"]

xNumpy = gd.buildNumpyArray(x)
yNumpy = gd.buildNumpyArray(y)

X = xNumpy.astype(numpy.float64)
y = yNumpy.astype(numpy.float64)
target_names = arr(["test1", "test2", "test3"])

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Percentage of variance explained for each components
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')

plt.show()