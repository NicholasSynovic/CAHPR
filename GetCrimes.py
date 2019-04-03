'''FILENAME: GetCrimes.py
LIBRARY NAME: CPD Crime Access
CREATED BY: Nicholas M. Synovic
GITHUB: https://www.github.com/nsynovic
LAST EDITED: 4/3/2019 14:09

ABSTRACTION: This libary uses the CPD Crimes OpenData Socrata API to download JSON files contating crime information.
'''

import json # Used to save JSON data to files
from urllib.request import urlopen  # Used to access and download JSON data 

class GetCrimes:
    '''ABSTRACTION: Class contains methods used to download and save JSON files.'''
    def __init__(self, appToken:str=None):
        '''ABSTRACTION:
PRE:
POST:
'''
        self.appToken = appToken    # Not needed, however better stability with it 

    def getAppToken(self)   ->  str:
        '''ABSTRACTION:
PRE:
POST:
'''
        return self.appToken

    def getOffset(self) ->  int:
        '''ABSTRACTION:
PRE:
POST:
'''
        return self.offset
    
    def getURLJSON(self, offset:int=None)   ->  dict:
        '''ABSTRACTION:
PRE:
POST:
'''
        self.setURLString(offset=offset)
        data = urlopen(url=self.getURLString())
        return json.load(fp=data)

    def getURLString(self) ->  str:
        '''ABSTRACTION:
PRE:
POST:
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