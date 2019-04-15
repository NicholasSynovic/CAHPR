import numpy
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
import Libs.program

run = Libs.program.Program()    # Title
run.uiApplicationToken()    # Gets Application Token
run.uiDownloadCrimeFiles()  # Downloads crime files
run.uiSetFileList()  # Finds every file in the downloads direct ory
run.checkForFeatures(files=run.getFiles())
print("\nAdding all of the crimes that occured in the same year to one file...")
run.aggregateByYear(files=run.getFiles())
print("\nCreating a list of all the crimes from that file...")
run.setAggregatedData(filename="2010crimes.json")
data = run.getAggregatedData()
print("\nCreating a rate of arrests per community area...")
arrestRate = run.rateInCommunityArea(data=data, key="arrest", value="True")
rateNonArrest = run.rateInCommunityArea(data=data, key="arrest", value="False")
print("\nCreating a rate of domestic disputes per community area...")
rateDomestic = run.rateInCommunityArea(data=data, key="domestic", value="True")
rateNonDomestic = run.rateInCommunityArea(data=data, key="domestic", value="False")
print("\nBuilding the data array to be analyzed...")
test = run.buildDictionary(arrest=arrestRate, nonArrest=rateNonArrest, domestic=rateDomestic, nonDomestic=rateNonDomestic, filename="Housing.csv")
xNumpy = run.convertIntoNumpy(dictionary=test)

X = xNumpy.astype(numpy.float64)

# Unless otherwise stated, the code below was taken from the SciKit-Learn documentation and/or modified/created by Dr. Mark V. Albert
pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)
print("\nBelow are the X, Y coordinates of each point on the graph...\n")    # By Nicholas Synovic
print(X_r)

print('\nThis is the explained variance ratio of the first two components: %s'
      % str(pca.explained_variance_ratio_))

plt.figure()
lw = 2

plt.scatter(X_r[:,0], X_r[:,1], alpha=.8, lw=lw)

plt.title('CAHPR PCA')

plt.autoscale() # By Nicholas Synovic

print("\nBelow are the weights of the components of the graph...\n")
print(pca.components_)

plt.show()
