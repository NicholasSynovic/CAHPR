import numpy
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
import Libs.program

run = Libs.program.Program()
run.setAggregatedData(filename="2010crimes.json")
data = run.getAggregatedData()
arrestRate = run.rateInCommunityArea(data=data, key="arrest", value="True")
rateNonArrest = run.rateInCommunityArea(data=data, key="arrest", value="False")
rateDomestic = run.rateInCommunityArea(data=data, key="domestic", value="True")
rateNonDomestic = run.rateInCommunityArea(data=data, key="domestic", value="False")
test = run.buildDictionary(arrest=arrestRate, nonArrest=rateNonArrest, domestic=rateDomestic, nonDomestic=rateNonDomestic, filename="Housing.csv")
xNumpy = run.convertIntoNumpy(dictionary=test)

X = xNumpy.astype(numpy.float64)

target_names = numpy.array(["test1", "test2", "negate me"])

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)
print(X_r)

print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

plt.figure()
lw = 2

plt.scatter(X_r[:,0], X_r[:,1], alpha=.8, lw=lw)

plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('CAHPR PCA')

plt.autoscale()
print(pca.components_)

plt.show()
