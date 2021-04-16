import matplotlib.pyplot as plt
import numpy
from sklearn.decomposition import PCA

import Libs.program

# Block is code that Nicholas M. Synovic has written
run = Libs.program.Program()    # Title
run.uiApplicationToken()    # Gets Application Token
run.uiDownloadCrimeFiles()  # Downloads crime files
run.uiSetFileList()  # Finds every file in the downloads directory
run.checkForFeatures(files=run.getFiles())
print("\nAdding all of the crimes that occured in the same year to one " +
      "file...")
run.aggregateByYear(files=run.getFiles())   # Gets a list of crimes that
# occured in the same year
print("\nCreating a list of all the crimes from that file...")
run.setAggregatedData(filename="2010crimes.json")   # Saves the crimes that
# occurred in the same year to a JSON file.
data = run.getAggregatedData()  # Gets the list of crimes that were aggregated
# in the same year
print("\nCreating a rate of arrests per community area...")
arrestRate = run.rateInCommunityArea(data=data, key="arrest", value="True")
# Gets the arrest rates in a community area
rateNonArrest = run.rateInCommunityArea(data=data, key="arrest", value="False")
# Gets the rate of crimes without arrest in a community area
print("\nCreating a rate of domestic disputes per community area...")
rateDomestic = run.rateInCommunityArea(data=data, key="domestic", value="True")
# Gets the rate of crimes that involved a domestic dispute in a community area
rateNonDomestic = run.rateInCommunityArea(data=data, key="domestic",
                                          value="False")
# Gets the rate of crimes that did not involve a domestic dispute.
print("\nBuilding the data array to be analyzed...")
test = run.buildDictionary(arrest=arrestRate, nonArrest=rateNonArrest,
                           domestic=rateDomestic, nonDomestic=rateNonDomestic,
                           filename="Housing.csv")
# Creates a dictionary of rates and housing data to be used for PCA
xNumpy = run.convertIntoNumpy(dictionary=test)  # Creates a numpy.array to be
# used for PCA analysis from the directory that was buiilt.
X = xNumpy.astype(numpy.float64)    # Changes the values of the numpy.array to
# that of floats

# Unless otherwise stated, this block of code came from "Comparison of LDA and
# PCA 2D projection of Iris dataset"
pca = PCA(n_components=2)   # Performs a 2D component analysis
X_r = pca.fit(X).transform(X)
print("\nBelow are the X, Y coordinates of each point on the graph...\n")
# By Nicholas Synovic
print(X_r)

print('\nThis is the explained variance ratio of the first two components: %s'
      % str(pca.explained_variance_ratio_))

plt.figure()
lw = 2
##
plt.scatter(X_r[:, 0], X_r[:, 1], alpha=.8, lw=lw)    # By Dr. Mark V. Albert
# Creates a scatter plot based off of the PCA data points.

plt.title('CAHPR PCA')  # Title of grpah

plt.autoscale()  # Autoscales the graph to fit all of the data.

print("\nBelow are the weights of the components of the graph...\n")
print(pca.components_)

plt.show()  # Shows the graph
