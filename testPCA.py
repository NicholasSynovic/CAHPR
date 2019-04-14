import numpy
import matplotlib.pyplot as plt

from numpy import array as arr
from sklearn import datasets
from sklearn.decomposition import PCA

import program

run = program.Program()
run.setAggregatedData(filename="2010crimes.json")
data = run.getAggregatedData()
arrestRate = run.rateInCommunityArea(data=data, key="arrest", value="True")
rateNonArrest = run.rateInCommunityArea(data=data, key="arrest", value="False")
rateDomestic = run.rateInCommunityArea(data=data, key="domestic", value="True")
rateNonDomestic = run.rateInCommunityArea(data=data, key="domestic", value="False")
test = run.buildDictionary(arrest=arrestRate, nonArrest=rateNonArrest, domestic=rateDomestic, nonDomestic=rateNonDomestic, filename="Housing.csv")
xNumpy = run.convertIntoNumpy(dictionary=test)

# gd = Libs.GetData.GetData(r"JSON\Crimes\crimes0.json")

# xNumpy = gd.makeNumpyArray(amount=1000)
# yNumpy = gd.buildNumpyArray(amount=1000, key="district", sort=True)

# X = xNumpy.astype(numpy.float64)
# y = yNumpy.astype(numpy.float64)

#xData = [['40','25','10'], ['5','16','20'], ['100','81','30'], ['120','14','40'], ['30','33','50'], ['10','27','60'], ['15','56','70'], ['20','73','80'], ['25','60','90']]
#yData = ['35000', '75000', '10000', '40000', '100000', '50000', '55000', '40000', '20000']

#xNumpy = numpy.array(xData)
#yNumpy = numpy.array(yData)

X = xNumpy.astype(numpy.float64)
# y = yNumpy.astype(numpy.float64)

target_names = numpy.array(["test1", "test2", "negate me"])

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)
print(X_r)

# Percentage of variance explained for each components
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

plt.figure()
lw = 2

plt.scatter(X_r[:,0], X_r[:,1], alpha=.8, lw=lw)
# for color, i, target_name in zip(colors, [0, 1,2], target_names):
#     plt.scatter(X_r[i, 0], X_r[i, 1], color=color, alpha=.8, lw=lw,
#                 label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')
plt.xlim((-100 * 500, 100 * 500))
plt.ylim((-100 * 500 ,100 * 500))
print(pca.components_)


plt.show()
