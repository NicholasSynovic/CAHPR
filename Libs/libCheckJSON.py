"""libCheckJSON.

CREATED BY Nicholas M. Synovic
GITHUB URL: https://www.github.com/nsynovic

ABSTRACTION: This library is meant to check a JSON file (that is a list containing dictionaries) for certain features (keys in the dictionaries).
"""

import json  # Used to manipulate JSON files


class CheckJSON:
    """A way to make sure JSON files have certain features present in them."""

    def __init__(self, features: list = []) -> None:
        """Starts the class with features to be searched for.

PRE: features is a list that contains the keys to be searched for in a JSON
file
POST: Creates a class variable containing the features
"""
        self.features = features

    def getFeatures(self) -> list:
        """Returns the features list.

PRE: No inputs
POST: Returns a list of features
"""
        return self.features

    def setFeatures(self, features: list) -> None:
        """Sets the feature list to be searched through.

PRE:
POST:
"""
        self.features = features

    def checkFileForFeatures(self, filename: str,
                             verbose: bool = True) -> bool or ["ERROR", int]:
        """Loops through the indices of a file and checks each index for keys.

PRE:
POST:
"""
        with open(file=filename) as file:
            data = json.load(fp=file)
            file.close()
        for x in range(len(data)):
            for key in self.features:
                if verbose:
                    try:
                        data[x][key]
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
