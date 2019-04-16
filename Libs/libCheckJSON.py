"""CREATED BY: Nicholas M. Synovic.

Parses a JSON file in order to make sure that certain keys exists in
said file.
"""

import json  # Used to manipulate JSON files


class CheckJSON:
    """Class to parse a JSON file."""

    def __init__(self, keys: list = []) -> None:
        """Function that initalizes the class and class variables.

PRE: keys is a list of keys to be searched for.
POST: Initalizes the class and sets features to a class variable.
"""
        self.keys = keys    # Is of type list.

    def getKeys(self) -> list:
        """Returns the list of keys to be searched for.

PRE: No inputs.
POST: Returns the list of keys to be searched for.
"""
        return self.keys    # Is of type list.

    def setKeys(self, keys: list = []) -> None:
        """Assigns a key list to the keys class variable.

PRE: keys is a list of keys to be searched for.
POST: The features class variable is assigned a new list of keys.
"""
        self.keys = keys    # Is of type list.

    def checkFileForFeatures(self, filename: str = "",
                             verbose: bool = False) -> bool or ["ERROR", int]:
        """Parses a JSON file in order to ensure that the keys exist.

PRE: filename is a string of the absolute or relatave path to a JSON file to be
parsed.
PRE: verbose is a boolean that if True, will display output for every parsed
crime in the file.
POST: Returns True if it parsed successfully, otherwise it returns a list
containg a string and the index of the crime in the file.
"""
        with open(file=filename) as file:
            data = json.load(fp=file)   # Is a list containg dictionaries
            file.close()
        for x in range(len(data)):
            for key in self.keys:   # Iterates through the list
                if verbose:
                    try:
                        data[x][key]    # If the data
                    except KeyError:
                        print(filename + " has a key error with key: " + key)
                        return ["ERROR", x]
                    print(filename + " has key: " + key + ", with value: " +
                          str(data[x][key]))
                else:
                    try:
                        data[x][key]
                    except KeyError:
                        return ["ERROR", x]
        return True
