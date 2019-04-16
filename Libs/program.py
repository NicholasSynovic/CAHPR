"""CREATED BY: Nicholas M. Synovic.

Functions that allow for user input to be handled across libraries.
"""

import Libs.libCheckJSON as CJ
import Libs.libDownloadJSON as DJ
import Libs.libGenerateJSON as GJ
import Libs.libListDirectoryFiles as LDF
import json  # Used to manipulate JSON files
import numpy    # Used to convert data types to a numpy.array
import os   # Used to manipulate underlying operating system commands


class Program:
    """Class for UI functionality across functions."""

    def __init__(self) -> None:
        """Function that initalizes the class and prints out a title.

PRE: No inputs.
POST: Initalizes the class and its' variables as well as it prints a title.
"""
        self.applicationToken = None
        self.files = None
        self.aggregatedData = None
        print("""Cluster Analysis in Relation to Housing Prices (CAHPR)
Project By: Nicholas Synovic, Laura Orrico, Eric Su, and Raul Azmitia""")

    def setAggregatedData(self, filename: str) -> None:
        """Assigns the contents of a json file to the aggregatedData variable.

PRE: filename is a string that points to the file location on disk.
POST: aggregatedData value is assigned the content of the file.
"""
        with open(file=filename) as file:   # Opens as read only
            self.aggregatedData = json.load(fp=file)

    def getAggregatedData(self) -> list:
        """Returns the value of the aggregatedData class variable.

PRE: No inputs.
POST: Returns the value of aggregatedData
"""
        return self.aggregatedData

    def getFiles(self) -> list:
        """Returns the value of the files class variable.

PRE: No inputs.
POST: The value of the class variable files is returned.
"""
        return self.files

    def setFiles(self, files: list) -> None:
        """Sets the class variable files to a list.

PRE: files is a list containing the path to JSON files on the disk to be
analyzed
POST: The class variables files is assigned the list of paths.
"""
        self.files = files

    def getApplicationToken(self) -> str:
        """Returns the value of the applicationToken variables.

PRE: No inputs.
POST: The value of applicationToken is returned.
"""
        return self.applicationToken

    def setApplicationToken(self, applicationToken: str) -> None:
        """Sets the value of applicationToken

PRE: applicationToken is the application token of the CPD OpenData Socrata API.
POST: The variable applicationToken is assigned the value.
"""
        self.applicationToken = applicationToken

    # Step 6
    def aggregateByYear(self, files: list, year: int = 2010) -> None:
        """Writes to a JSON file every crime that occured in a given year.

PRE: files is a list of file paths on disk.
PRE: year is an integer that determines the name of the output file and what
crimes to be added to said file.
POST: A JSON file is written to disk containing all the crimes that happened
in a given year.
"""
        output = str(year) + "crimes.json"
        try:
            with open(file=output) as test:
                test.close()
            os.remove(output)
        except FileNotFoundError:
            pass
        parser = GJ.Generator(key="year")
        for x in files:
            parser.getDataFromFile(filename="Crimes\\" + x)
            parser.addToList(data=parser.getData())
        parser.writeListToFile(filename=output)

    # Step 5
    def checkForFeatures(self, files: list, features: list =
                         ["arrest", "community_area",
                          "domestic", "year"]) -> None:
        """Parses through JSON files looking for required features.

PRE: files is a list of paths to files on disk that will be parsed.
PRE: features is a list of keys that will be searched for in each file.
"""
        checker = CJ.CheckJSON(keys=features)
        for x in files:
            print("Testing for key features in file: Crimes\\" + x)
            test = checker.checkFileForFeatures(filename=r"Crimes\\" + x,
                                                verbose=False)
            if test:
                print("Test passed")
            else:
                print("Error at index: " + str(test[1]) + "in file " + x)
                quit(1)

    def downloadFiles(self, maxAmount: int) -> None:
        """Downloads files from the CPD OpenData Socrata API.

PRE: maxAmount is the amount of files that will be downloaded.
POST: The amount of files dictated by maxAmount are downloaded to the Crimes
folder of the project.
"""
        ldj = DJ.GetCrimes(appToken=self.getApplicationToken(), offset=0)
        print("\n")     # new line
        for x in range(maxAmount):
            filename = r"Crimes\crimes" + str(x) + ".json"
            ldj.setURL(offset=x*1000)
            ldj.setJSON()    # Downloads json
            data = ldj.getJSON()  # Makes json viewable
            ldj.saveJSON(filename=filename, data=data)
            outcome2 = ldj.getURL()
            print("Downloaded file: " + str(outcome2))

    # Step 4
    def uiSetFileList(self) -> None:
        """Sets the files variable to a list of paths of JSON files.

PRE: No inputs.
POST: The files class variable is assigned a list of paths to JSON files in the
Crimes directory in the project folder.
"""
        print("Creating list of files in directory Crimes...")
        f = LDF.GetFiles(directory="Crimes").getFileList()
        self.files = f

        # Step 3
    def uiDownloadCrimeFiles(self) -> None:
        """Asks the user if they want to download the crime files.

PRE: No input.
POST: Files are downloaded based off of the user's input.
"""
        while True:
            question1 = input("\nDo you want to download the necessary crime" +
                              " files needed for this application " +
                              "(Y/N)? ").lower()
            if question1 == "n":
                break
            elif question1 == "y":
                while True:
                    try:
                        maxAmount = int(input("""\nHow many crime files do you want to download?
NOTE: Each crime file has 1000 individual crimes in it. """))
                        break
                    except ValueError:
                        print("""\nInvalid input.
Type in an integer this time...""")
                # Step 4
                self.downloadFiles(maxAmount=maxAmount)
                break
            else:
                print("""\nInvalid input.
Type Y or N this time...""")

    # Step 2
    def uiApplicationToken(self) -> None:
        """Asks the user for their app token for the CPD OpenData Socrata API.

PRE: No inputs.
POST: The inputted application token is stored in the applicationToken
variable.
"""
        aT = ""
        while True:
            question1 = input("\nDo you have an application token for the " +
                              "CPD Crimes OpenData Socrata API" +
                              " (Y/N)? ").lower()
            if question1 == "n":
                break
            elif question1 == "y":
                aT = str(input("\nWhat is your application token? "))
                break
            else:
                print("""\nInvalid input.
Type Y or N this time...""")
        self.setApplicationToken(applicationToken=aT)

    # DOES NOT WORK AT THE MOMENT
    # def rateInCity(self, data: list, key: str, value: str):
    #     rates = {}
    #     total = 0
    #     count = 0
    #
    #     for x in range(78):
    #         if x == 0:
    #             pass
    #         else:
    #             for y in data:
    #                 try:
    #                     for z in list(y.keys()):
    #                         if z == key:
    #                             total += 1
    #                     if y["community_area"] == str(x):
    #                         if str(y[key]) == value:
    #                             count += 1
    #                             break
    #                 except KeyError:
    #                     pass
    #             rates[str(x)] = str((count / total) * 100)
    #     return rates

    # Step 9 # Makes the dictionary containg all the values associated with a
    # community area
    def buildDictionary(self, arrest: dict, nonArrest: dict, domestic: dict,
                        nonDomestic: dict, filename: str) -> dict:
        """Creates a dictionary of rates and housing data to be used for PCA.

PRE: arrest is a dictionary of rates of crimes that involved arrests.
PRE: nonArrest is a dictionary of rates of crimes that did not involve arrests.
PRE: domestic is a dictionary of rates of crimes that involved domestic
disputes.
PRE: nonDomestic is a dictionary of rates of crimes that did not invilve
domestic disputes.
PRE: filename is the path to a CSV file containg the housing information to be
used for PCA.
POST: A dictionary is returned containg lists of data points per community area
in Chicago.
"""
        dictionary = {}
        rowData = []
        # https://stackoverflow.com/questions/13428318/reading-rows-from-a-csv-
        # file-in-python the unfun cat
        for line in open(file=filename):
            rowData.append(line.strip().split(","))

        for x in range(78):
            values = []
            if x == 0:
                pass
            else:
                values.append(arrest[str(x)])
                values.append(nonArrest[str(x)])
                values.append(domestic[str(x)])
                values.append(nonDomestic[str(x)])
                for y in rowData:
                    if y[0] == str(x):
                        for z in range(len(y)):
                            if z == 0:
                                pass
                            else:
                                values.append(y[z])
                        break
                dictionary[str(x)] = values
        return dictionary

    # Step 7
    def rateInCommunityArea(self, data: list, key: str, value: str) -> dict:
        """Creates a dictionary of a rate in a community area.

PRE: data is a list of crimes.
PRE: key is a string that tells the parser to create a rate of a given key in
the list of crimes.
PRE: value is a string that tells the parser to create a rate of a community
area only if the value of the key is equivalant to the parameter.
POST: A dictionary of rates (where the community area is the key and the value
is the rate).
"""
        rates = {}
        total = 0
        count = 0
        for x in range(78):
            if x == 0:
                pass
            else:
                for y in data:
                    try:
                        if y["community_area"] == str(x):
                            for z in list(y.keys()):
                                if z == key:
                                    total += 1
                                    if str(y[key]) == value:
                                        count += 1
                                        break
                    except KeyError:
                        pass
                rates[str(x)] = str((count / total) * 100)
        return rates

    # FINAL STEP
    def convertIntoNumpy(self, dictionary: dict) -> numpy.array:
        """Turns a dictionary into a numpy.array.

PRE: dictionary is a dictionary of values to be turned into a numpy.array
POSTT: A numpy.array of the dictionary is returned.
"""
        data = list(dictionary.values())
        return numpy.array(data)
