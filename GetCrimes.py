'''FILENAME: GetCrimes.py
CREATED BY: Nicholas M. Synovic
GITHUB URL: https://www.github.com/nsynovic

ABSTRACTION: This libary uses the CPD Crimes OpenData Socrata API to download JSON files contating crime reports.
'''
import json # Used to save JSON data to files.
from urllib.request import urlopen  # Used to access and download JSON data.


class NoAppToken(Exception):
    '''ABSTRACTION: Custom exception only to be used if the user does not enter an app token at all.
'''
    pass

class GetCrimes:
    '''ABSTRACTION: Should be used to create a tunnel to the OpenData Socrate API to get crime reports.
'''
    def __init__(self, appToken:str=None, offset:int=None) ->  None:
        '''ABSTRACTION: Starts the class with or without an OpenData app token, and initializes class variables.
PRE: Takes in an app token string.
POST: Creates a class variable that contains the app token and all other needed class variables with their default values.
'''
        try:
            if appToken is not None:
                self.appToken = appToken    # Used for a more stable connection with the OpenData Socratic API enpoint.
            else:
                raise NoAppToken
            if offset is not None:
                self.offset = offset    # This is where the crime count will start from (i.e get crimes after the 50th [offest=50] crime).
            else:
                self.offset = 0
        except NoAppToken:
            print("""No app token.
Get a valid app token at: https://data.cityofchicago.org/profile/app_tokens
""")    # Valid link for getting an app token as of 4-08-2019.
            quit(code=1)
        self.url = r"https://data.cityofchicago.org/resource/6zsd-86xi.json?$$app_token=" + self.appToken + "&$offset=" + str(self.offset)# The actual URL of the endpoint.
        self.json = {}

    def getAppToken(self)   ->  str:
        '''ABSTRACTION: Returns the app token class variable
PRE: No inputs.
POST: Returns app token class variable.
'''
        return self.appToken

    def getJSON(self)   ->  dict:
        '''ABSTRACTION: Returns the current data stored in the json class variable. This data is highly volitile and could be wiped if setJSON() is run.
PRE: No inputs.
POST: Returns the json class variable.
'''
        return self.json

    def getOffset(self) ->  int:
        '''ABSTRACTION: Returns the offset class variable.
PRE: No inputs.
POST: Returns offset class variable.
'''
        return self.offset

    def getURL(self) ->  str:
        '''ABSTRACTION: Returns the url class variable.
PRE: No inputs.
POST: Returns url class variable.
'''        
        return self.url

    def saveJSON(self, filename:str=None, data:dict=None)   ->  [str, bool]:
        '''ABSTRACTION: Saves the json class variable's data to a .json file to prevent the data currently being stored from being deleted if setJSON() is run.
PRE: filename is the .json filename or filepath of where the json class variables data will be stored.
PRE: data is the json data to be stored in the file.
POST: A .json file with the name of [filename] is created and a return array containg the filename and whether or not the data was stored (the latter will be a boolean: True means data was stored).
'''
        try:
            with open(file=filename, mode="w") as save:
                json.dump(obj=data, fp=save)
            return [filename, True]
        except IOError:
            return [filename, False]

    def setAppToken(self, appToken:str="")  ->  None:
        '''ABSTRACTION: Sets the class variable appToken to a different value.
PRE: appToken is used for a more stable connection with the OpenData Socratic API enpoint.
POST: Sets appToken class variable to a different value.
'''
        self.appToken = appToken

    def setJSON(self)   ->  None:
        '''ABSTRACTION: Stores crime data from in a dictionary in memory. This method should be called on its own (not assigned to a variable).
PRE: offset is where the crime count will start from (i.e get crimes after the 50th [offest=50] crime).
POST: Stores the crime report JSON in a dictionary.
'''
        data = urlopen(url=self.getURL())
        self.json = json.load(fp=data)

    def setOffset(self, offset:int=0)   ->  None:
        '''ABSTRACTION: Sets the class variable offset to a different value.
PRE: offset is where the crime count will start from (i.e get crimes after the 50th [offest=50] crime).
POST: Sets offset class variable to a different value.
'''
        self.offset = offset
    
    def setURL(self, appToken:str="", offset:int=0)    ->  None:
        '''ABSTRACTION: Sets the class variable url to a different value by changing what app token and offset is inputted (if at all). 
PRE: appToken is used for a more stable connection with the OpenData Socratic API enpoint. If None, the class variable will be used.
PRE: offset is where the crime count will start from (i.e get crimes after the 50th [offest=50] crime). If None, the class variable will be used.
POST: Sets url class variable to a different value.
'''
        self.appToken = appToken
        self.offset = offset
        self.url = r"https://data.cityofchicago.org/resource/6zsd-86xi.json?$$app_token=" + self.appToken + "&$offset=" + str(self.offset)  # Creates an endpoint url