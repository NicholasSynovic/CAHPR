'''FILENAME: GetCrimes.py
CREATED BY: Nicholas M. Synovic
GITHUB URL: https://www.github.com/nsynovic

ABSTRACTION: This libary uses the CPD Crimes OpenData Socrata API to download JSON files contating crime reports.
'''
import json # Used to save JSON data to files.
from urllib.request import urlopen  # Used to access and download JSON data.


class GetCrimes:
    '''ABSTRACTION: Creates a tunnel to the OpenData Socrate API to get crime reports.
'''
    def __init__(self, appToken:str="")   ->  None:
        '''ABSTRACTION: Starts the class with or without an OpenData app token, and initializes class variables.
PRE: Takes in an app token string.
POST: Creates a class variable that contains the app token and all other needed class variables with their default values.
'''
        self.appToken = appToken    # Not needed, however better stability with it.
        self.offset = 0
        self.url = ""
        self.json = {}
        
    def getAppToken(self)   ->  str:
        '''ABSTRACTION: Returns the app token class variable
PRE: No inputs.
POST: Returns app token class variable.
'''
        return self.appToken

    def getOffset(self) ->  int:
        '''ABSTRACTION: Returns the offset class variable.
PRE: No inputs.
POST: Returns offset class variable.
'''
        return self.offset
    
    def setJSON(self, offset:int=0)   ->  None:
        '''ABSTRACTION: Stores crime data from in a dictionary in memory. 
PRE: offset is where the crime count will start from (i.e get crimes after the 50th [offest=50] crime).
POST: Stores the crime report JSON in a dictionary.
'''
        self.setURLString(offset=offset)
        data = urlopen(url=self.getURLString())
        self.json = json.load(fp=data)
        
    def getURLString(self) ->  str:
        '''ABSTRACTION: Returns the url class variable.
PRE: No inputs.
POST: Returns url class variable.
'''        
        return self.url

    def saveJSON(self, filename:str=None, data:dict=None)   ->  [str, bool]:
        '''ABSTRACTION:
PRE:
POST:
'''
        try:
            with open(file=filename, mode="w") as save:
                json.dump(obj=data, fp=save)
            return [filename, True]
        except IOError:
            return [filename, False]

    def setOffset(self, offset:int=None) ->  None:
        '''ABSTRACTION:
PRE:
POST:
'''
        self.offset = offset
    
    def setAppToken(self, appToken:str=None)    ->  None:
        '''ABSTRACTION:
PRE:
POST:
'''
        self.appToken = appToken
    
    def setURLString(self, offset:int=None)  ->  None:
        '''ABSTRACTION:
PRE:
POST:
'''
        self.offset = offset
        self.url = r"https://data.cityofchicago.org/resource/6zsd-86xi.json?$$app_token=" + self.appToken + "&$offset=" + str(self.offset)
