# Cluster Analysis of Housing Prices in Relation to Crime (CAHPR)

Cluster Analysis of Housing Prices in Relation to Crime (CAHPR) is a student led project to analyze both crime and housing data to find assess different factors that impact housing prices in the city of Chicago, Illinois in the year 2010. This project takes advantage of Primary Component Analysis (PCA) to assess the impact of four crime related factors and four housing related factors. This project was created at Loyola University Chicago and by (in no particular order): Nicholas Synovic, Laura Orrico, Eric Su, and Raul Azmitia.

## Getting Started

To view our project, you will need [Python 3.7.3](https://www.python.org/) installed on your computer. If it is not installed on your computer, head to the [Python Downloads page](https://www.python.org/downloads/release/python-373/) and download the version compatible with your computer's archetecture. Furthermore, you will need to download the most current release of our project. You can either: 
* A) Clone the repository to your local machine 
* B) Go to the [Releases tab](https://github.com/NicholasSynovic/Cluster-Analysis-of-Housing-Prices-in-Relation-to-Crime/releases) and download the most current release of our project. 
  * **NOTE:** If you do download our project from the [Releases tab](https://github.com/NicholasSynovic/Cluster-Analysis-of-Housing-Prices-in-Relation-to-Crime/releases), make sure that your computer is capable of opening .ZIP files.

### Prerequisites

After downloading the required files as described above, you will need to configure your Python 3.7.3 environment to allow the program to run. To do this open Command Prompt or Terminal in the project directory and type:

```
pip install -r requirements.txt
```

This will install the [Matplotlib](https://matplotlib.org/), [Numpy](http://www.numpy.org/), and [Scikit-Learn](https://scikit-learn.org/stable/) modules onto your computer. 
  * **NOTE:** We highly recomend that these modules are installed in a virtual environment for Python 3.7.3. As it is not a requirement to run the project, we will thus not provide instructions for setting one up. However if you are interested in setting up a virtual environment, please visit [this link](https://docs.python-guide.org/dev/virtualenvs/) for more instructions.

## Running CAHPR

To run CAHPR simply open Command Prompt or Terminal in the root of the project directory and run:

```
python "CAHPR PCA.py"
```

  * **NOTE:** Depending on how you installed Python 3.7.3, this command might fail. If it does use this command instead:

```
PATH\TO\PYTHON\3.7.3\python.exe "CAHPR PCA.py"
```

After typing in the command, follow the instructions that pop up in the terminal and wait for the output.

### Developing CAHPR or Expanding CAHPR's Functionality

If you are so inclined as to develop CAHPR or expand its functionality, please make sure that you are following [Python PEP 8 Style Guidelines](https://www.python.org/dev/peps/pep-0008/). This is to promote easy readability across developers. Furthermore, please consult our [LISCENSE](LICENSE) file for more information on copyright and liscensing agreements.

## Built With

* [Python 3.7.3](https://www.python.org/downloads/release/python-373/)
* [Matplotlib](https://matplotlib.org/)
* [Numpy](http://www.numpy.org/)
* [SciKit-Learn](https://scikit-learn.org/)

## Authors

* **Nicholas Synovic**
* **Laurua Orrico**
* **Eric Su**
* **Raul Azmitia**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Dr. Mark V. Albert without whom we would not have created an accurate PCA graph. You can view his CV here.
* [SciKit-Learn's "Comparison of LDA and PCA 2D projection of Iris dataset" Article](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html) which is where the starting point for our PCA code came from.
* The [Chicago Police Department](https://home.chicagopolice.org/) for whom released the crime data that we used for this project. You can view it [here](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2).
* The [Chicago Metropolitan Agency For Planning (CMAP)](https://www.cmap.illinois.gov/) for whom collected and aggregated 2010 housing data in Chicago, Illinois. You can view it [here](https://www.cmap.illinois.gov/data/demographics/census/2010-census-analysis).
* [Frank Hoffman](https://twitter.com/hofmannedv) over at [Stack Abuse](https://stackabuse.com/) for providing code for iterating through a directory of files. You can view it [here](https://stackabuse.com/python-list-files-in-a-directory/).
* [The Unfun Cat](https://stackoverflow.com/users/992687/the-unfun-cat) at [Stack Overflow](https://stackoverflow.com/) for writing code to extract CSV rows as a single list. You can view it [here](https://stackoverflow.com/a/13428369/11229402).
