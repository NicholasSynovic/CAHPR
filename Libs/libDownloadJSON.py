"""GetCrimes.

CREATED BY: Nicholas M. Synovic
GITHUB URL: https://www.github.com/nsynovic

This library uses the CPD Crimes OpenData Socrata API to download JSON files
contacting crime reports.
"""

import json  # Used to save JSON data to files.
from urllib.request import urlopen  # Used to access and download JSON data.


class NoAppToken(Exception):
    """Exception to be used if the user does not enter an application token."""

    pass


class GetCrimes:
    """Uses the OpenData Socrate API to get crime reports."""

    def __init__(self, appToken: str = None, offset: int = None) -> None:
        """Starts the class with or without an OpenData application token.

PRE: appToken is used for a more stable connection with the OpenData Socrata
API end point.
PRE: offset is where the crime count will start from (i.e get crimes after the
50th [offset=50] crime).
POST: Creates a class variable that contains the application token and all
other needed class variables with their default values.
"""
        try:
            if appToken is not None:
                self.appToken = appToken    # Used for a more stable connection
                # with the OpenData Socrata API end point.
            else:
                raise NoAppToken
            if offset is not None:
                self.offset = offset    # This is where the crime count will
                # start from (i.e get crimes after the 50th [offset=50] crime).
            else:
                self.offset = 0
        except NoAppToken:
            print("""No application token.
Get a valid app token at: https://data.cityofchicago.org/profile/app_tokens
""")    # Valid link for getting an application token as of 4-08-2019.
            quit(code=1)
        self.url = ("https://data.cityofchicago.org/resource/6zsd-86xi.json?" +
                    "$$app_token=" + self.appToken + "&$offset=" +
                    str(self.offset))  # The actual URL of the end point.
        self.json = {}

    def getAppToken(self) -> str:
        """Returns the application token class variable.

PRE: No inputs.
POST: Returns application token class variable.
"""
        return self.appToken

    def getJSON(self) -> dict:
        """Returns the current data stored in the JSON class variable.

This data is highly volatile and could be wiped if setJSON() is run.
PRE: No inputs.
POST: Returns the JSON class variable.
"""
        return self.json

    def getOffset(self) -> int:
        """Returns the offset class variable.

PRE: No inputs.
POST: Returns offset class variable.
"""
        return self.offset

    def getURL(self) -> str:
        """Returns the URL class variable.

PRE: No inputs.
POST: Returns URL class variable.
"""
        return self.url

    def saveJSON(self, filename: str = None, data: dict = None) -> [str, bool]:
        """Saves the JSON class variable's data to a .JSON file.

PRE: filename is the .JSON filename or file path of where the JSON class
variables data will be stored.
PRE: data is the JSON data to be stored in the file.
POST: A .JSON file with the name of [filename] is created and a return array
containing the filename and whether or not the data was stored
(the latter will be a boolean: True means data was stored).
"""
        try:
            with open(file=filename, mode="w") as save:
                json.dump(obj=data, fp=save)
            return [filename, True]
        except IOError:
            return [filename, False]

    def setAppToken(self, appToken: str = "") -> None:
        """Sets the class variable appToken to a different value.

PRE: appToken is used for a more stable connection with the OpenData Socrata
API end point.
POST: Sets appToken class variable to a different value.
"""
        self.appToken = appToken

    def setJSON(self) -> None:
        """Stores crime data from in a dictionary in memory.

This method should be called on its own (not assigned to a variable).
PRE: offset is where the crime count will start from
(i.e get crimes after the 50th [offset=50] crime).
POST: Stores the crime report JSON in a dictionary.
"""
        data = urlopen(url=self.getURL())
        self.json = json.load(fp=data)

    def setOffset(self, offset: int = 0) -> None:
        """Sets the class variable offset to a different value.

PRE: offset is where the crime count will start from
(i.e get crimes after the 50th [offset=50] crime).
POST: Sets offset class variable to a different value.
"""
        self.offset = offset

    def setURL(self, offset: int = 0) -> None:
        """Sets the class variable URL to a different value.

PRE: appToken is used for a more stable connection with the OpenData Socrata
API end point. If None, the class variable will be used.
PRE: offset is where the crime count will start from
(i.e get crimes after the 50th [offset=50] crime).
If None, the class variable will be used.
POST: Sets URL class variable to a different value.
"""
        self.offset = offset
        self.url = ("https://data.cityofchicago.org/resource/6zsd-86xi.json?" +
                    "$$app_token=" + self.appToken + "&$offset=" +
                    str(self.offset))  # Creates an end point URL
