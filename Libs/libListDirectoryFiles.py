"""CREATED BY: Nicholas M. Synovic.

Parses a directory and provides functions to look at the paths of files int the
directory.
"""

import os  # Used to parse a directory on disk


class GetFiles:
    """Class to parse a directory."""

    def __init__(self, directory: str) -> None:
        """Function to initalizes the class.

PRE: directory is a string of the path to a directory on disk.
POST: Initalizes the class and sets values to class variables.
"""
        self.directory = directory  # A string
        self.data = []  # A list

    def getData(self) -> list:
        """Returns the class variable data.

PRE: No inputs.
POST: The value of data is returned.
"""
        return self.data

    def setData(self, data: list) -> None:
        """Assigns a value to the class variable data.

PRE: data is a list to be assigned to the class variable.
POST: Sets the value of data to a list.
"""
        self.data = data

    def getDirectory(self) -> str:
        """Returns the directory path from the directory class variable.

PRE: No inputs.
POST: The directory to be parsed will be returned.
"""
        return self.directory

    def setDirectory(self, directory: str) -> None:
        """Sets the value of the class variable directory.

PRE: directory is a string that should be the path to a directory on disk.
POST: The value of the class variable directory is assigned.
"""
        self.directory = directory

    def getDataLength(self) -> int:
        """Returns the length of the class variable data.

PRE: No inputs.
POST: Returns the length of the variable.
"""
        return len(self.data)

    def getListLength(self, data: list) -> int:
        """Returns the length of a list.

PRE: data is a list to be whose length is to be returned.
POST: returns the length of the parameter.
"""
        return len(data)

    def getFileList(self) -> list:
        """Returns a list of files in a directory.

PRE: No inputs.
POST: A list of every filename in a directory.
"""
        data = []
        # For loop code taken from:
        # https://stackabuse.com/python-list-files-in-a-directory/
        for root, dirs, files in os.walk(self.directory):
            for x in range(len(files)):
                data.append(files[x])
        return data
