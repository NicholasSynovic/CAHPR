import Libs.libCheckJSON as CJ
import Libs.libDownloadJSON as DJ
import Libs.libGenerateJSON as GJ
import Libs.libListDirectoryFiles as LDF
import json
import numpy


class Program:

    def __init__(self):
        self.applicationToken = None
        self.files = None
        self.aggregatedData = None
        print("""Cluster Analysis in Relation to Housing Prices (CAHPR)
Project By: Nicholas Synovic, Laura Orrico, Eric Su, and Raul Azmitia""")

    def setAggregatedData(self, filename: str):
        with open(file=filename) as file:
            self.aggregatedData = json.load(fp=file)

    def getAggregatedData(self):
        return self.aggregatedData

    def getFiles(self):
        return self.files

    def setFiles(self, files: list):
        self.files = files

    def getApplicationToken(self) -> str:
        return self.applicationToken

    def setApplicationToken(self, applicationToken: str) -> None:
        self.applicationToken = applicationToken

    # Step 6
    def aggregateByYear(self, files: list, year: int = 2010):
        parser = GJ.Generator(key="year")
        for x in files:
            parser.getDataFromFile(filename="Crimes\\" + x)
            parser.addToList(data=parser.getData())
        parser.writeListToFile(filename=str(year) + "crimes.json")

    # Step 5
    def checkForFeatures(self, files: list, features: list =
                         ["arrest", "community_area", "domestic", "year"]):
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

    # Step 3
    def downloadFiles(self, maxAmount: int) -> None:
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
    def uiSetFileList(self):
        print("Creating list of files in directory Crimes...")
        f = LDF.GetFiles(directory="Crimes").getFileList()
        self.files = f
        print(type(self.files))

        # Step 3
    def uiDownloadCrimeFiles(self) -> None:
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
        aT = ""
        while True:
            question1 = input("\nDo you have an application token for the CPD" +
                              "Crimes OpenData Socrata API (Y/N)? ").lower()
            if question1 == "n":
                break
            elif question1 == "y":
                aT = str(input("\nWhat is your application token? "))
                break
            else:
                print("""\nInvalid input.
Type Y or N this time...""")
        self.setApplicationToken(applicationToken=aT)

    # Step 8 DOES NOT WORK AT THE MOMENT
    def rateInCity(self, data: list, key: str, value: str):
        rates = {}
        total = 0
        count = 0

        for x in range(78):
            if x == 0:
                pass
            else:
                for y in data:
                    try:
                        for z in list(y.keys()):
                            if z == key:
                                total += 1
                        if y["community_area"] == str(x):
                            if str(y[key]) == value:
                                count += 1
                                break
                    except KeyError:
                        pass
                rates[str(x)] = str((count / total) * 100)
        return rates


    # Step 9 # Makes the dictionary containg all the values associated with a
    #community area
    def buildDictionary(self, arrest: dict, nonArrest: dict, domestic: dict,
                        nonDomestic: dict, filename: str):
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
    def rateInCommunityArea(self, data: list, key: str, value: str):
        rates = {}  # Needed to return dictionary
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

    # FINALL FUCKING STEP
    def convertIntoNumpy(self, dictionary: dict):
        data = list(dictionary.values())
        return numpy.array(data)
