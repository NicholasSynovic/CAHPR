"""CREATED BY: Nicholas M. Synovic.

Library to parse and format JSON data into CSV and numpy.array
data structures.
"""
import json  # Needed to parse through data

import numpy  # Needed to output a numpy.array


class GetData:
    """Used to format the crime JSON data into different data structures."""

    def __init__(self, filename: str) -> None:
        """Loads JSON data from a .json file and into an array.

PRE: filename is a file that has crime data from the CPD OpenData Socratic API.
Typically this would be found in JSON/Crimes
POST: Creates jsonData and filename class variables.
"""
        self.filename = filename
        try:
            with open(file=self.filename) as file:
                self.data = json.load(fp=file)
            file.close()
        except IOError:
            print("Invalid filename: " + str(self.filename))
            quit(code=1)
        self.parsedDict = {}

    def addToParsedDict(self, key: str, value: str) -> None:
        """Adds a key value pair to the parsedDict class variable.

Will change a keys value if a key is already signed a value
PRE: key is a string that will be the key added to parsedDict.
PRE: value is a string that will be the value added to parsedDict.
POST: parsedDict is updated with the new key value pair.
"""
        self.parsedDict[key] = value

    def getCrimeSpecificInfo(self, index: int = 0, key: str = "") -> dict:
        """Returns a dictionary.

PRE: index is an int that tells what crime should be parsed for data
(min = 0, max = 999).
PRE: key is a string that will be used to find a matching key in a crime and
extropolate that data.
POST: Returns a dictionary containg explicitly the key value pair for a
specific crime.
"""
        crime = self.getSpecificCrime(index=index)
        try:
            return {key: crime[key]}
        except KeyError:    # Invalid key inputted
            print("Invalid key: " + str(key) + ", " + self.filename)
            quit(code=1)

    def getData(self) -> list:
        """Returns every crime that can be worked on.

PRE: No inputs.
POST: Returns a list of crimes formatted as a dictionary.
"""
        return self.data

    def getFilename(self) -> str:
        """Returns the filename of the current working file.

PRE: No inputs.
POST: Returns the filename as a string.
"""
        return self.filename

    def getKeys(self, dictionary: dict) -> list:
        """Returns the keys of a dictionary in an iterable list.

PRE: dictionary is the dictionary to be parsed through for keys.
POST: a list is returned with all and only the dictionary keys.
"""
        return list(dictionary.keys())

    def getParsedDict(self) -> dict:
        """Returns the parsedDict class variable

PRE: No inputs.
POST: Returns the dictionary
"""
        return self.parsedDict

    def getSpecificCrime(self, index: int = 0) -> dict:
        """Returns all the data associated with one crime.

PRE: index is an int that tells what crime should be parsed for data
(min = 0, max = 999).
POST: returns a dictionary containing all the data for a given crime.
"""
        return self.getData()[index]

    def getValues(self, dictionary: dict) -> list:
        """Returns the values of a dictionary in an iterable list.

PRE: dictionary is the dictionary to be parsed through for values.
POST: a list is returned with all and only the dictionary values.
"""
        return list(dictionary.values())

    def setData(self, filename: str = None) -> None:
        """Opens a new file and changes what crimes can be worked on.

PRE: filename is a string that should be the relative path to a given file.
POST: the filename class variable is changed and the data class variable is
updated to have all the crimes from the file that filename points to.
"""
        if filename is not None:
            self.filename = str(filename)
        try:
            with open(file=self.filename) as load:
                self.data = json.load(fp=load)
            load.close()
        except IOError:
            print("Invalid filename: " + str(self.filename))
            quit(code=1)

    def setFilename(self, filename: str) -> None:
        """Changes the filename class variable to a different value.

PRE: filename is a string that should be the relative path to a given file.
POST: the filename class variable's value is changed.
"""
        self.filename = filename

    def setParsedDict(self, data: dict) -> None:
        """Changes the data in the parsedDict class variable to something

entirely different.
WARNING: this wil delete any values associated with the variable
PRE: data is a dictionary to replace the key value pairs in parsedDict
POST: parsedDict's key value pairs are replaced with those of data
"""
        self.parsedDict = data

    def makeNumpyArray(self, amount: int) -> numpy.array:
        """Creates a numpy array from a dictionary.

PRE: amount is an int that represents how many crimes you want to have in
your numpy array.
PRE: keys is a list of strings that represents what key values you want in
your numpy array.
POST: returns a numpy array.
"""
        keys = ["beat", "community_area", "year"]  # Change these once a
# descision has been made on what they should be
        root = []
        for x in range(amount):
            dataList = []
            for key in keys:
                try:
                    index = keys.index(key)
                except ValueError:
                    print("Invalid key: " + key)
                    quit(code=1)
                data = self.getCrimeSpecificInfo(index=x, key=str(key))
                value = self.getValues(dictionary=data)
                dataList.insert(index, str(value[0]))
            root.insert(x, dataList)
        return numpy.array(object=root)

    def buildNumpyArray(self, amount: int,
                        key: str,
                        sort: bool = False) -> numpy.array:
        """Makes a numpy array of only one key. Useful for making the y values.

PRE: amount is an int that represents how many crimes should be analyzed for
the given key.
PRE: key is a string that represents the key to be found for a given crime.
PRE: sort is a boolean which sorts the data frin least to greatest.
POST: Returns a numpy.array in either sorted or unsorted order.
"""
        root = []
        for x in range(amount):
            data = self.getCrimeSpecificInfo(index=x, key=str(key))
            value = self.getValues(dictionary=data)
            root.insert(x, str(value[0]))
        if sort:
            root = sorted(root)
        return numpy.array(object=root)
