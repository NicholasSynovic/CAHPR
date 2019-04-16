"""CREATED BY: Nicholas M. Synovic.

Creates a JSON file from a list.
"""

import json  # Used to manipulate JSON files


class Generator:
    """Class to create JSON files."""

    def __init__(self, key: str) -> None:
        """Function that initalizes the class and its class variables.

PRE: key is a string that represents what key to be searched for.
POST: The class is initalized.
"""
        self.key = key
        self.data = []  # Used to store JSON data
        self.mega = []  # Used to write to a JSON file

    def getData(self):
        """Returns the value of the class variable data

PRE: No inputs.
POST: Returns the value of the variable.
"""
        return self.data

    def getDataFromFile(self, filename: str) -> None:
        """Sets the value of the class variable data to the contents of a file.

PRE: filename is the path to a file on disk.
POST: The class variable data is assigned the contents of a file.
"""
        with open(file=filename) as file:
            self.data = json.load(fp=file)
            file.close()

    def searchForValue(self, value) -> list:
        """Returns a list of crimes that share a value in a given key.

PRE: value is any value that you want to search for in a crime.
POST: Returns the list of crimes that have a valid value.
"""
        root = []
        for x in range(len(self.data)):
            if self.data[x][self.key] == value:
                root.insert(x, self.data[x])
        return root

    def addToList(self, data: list) -> None:
        """Appends the values of a list to a larger list.

PRE: data is the list to be appended to to the class varible mega.
POST: Sets the value of mega to that of every value in data.
NOTE: This does not clear the varaible mega, it just apends data to it.
"""
        for x in range(len(data)):
            self.mega.append(data[x])

    def writeListToFile(self, filename: str = "agregatedCrimes.json") -> None:
        """Writes data from the variable mega to a JSON file.

PRE: filename is the directory of the JSON file to be written to.
POST: Data is written to the file.
NOTE: Data is appeneded to the file, the file is not overwritten.
"""
        with open(file=filename, mode="a") as file:
            json.dump(obj=self.mega, fp=file)
            file.close()
