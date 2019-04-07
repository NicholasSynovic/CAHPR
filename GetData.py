import json
import csv
import numpy

class GetData:

    def __init__(self, filename:str)    ->  None:
        self.filename = filename
        with open(file=self.filename, mode="r") as file:
            self.jsonData = json.load(fp=file)
        file.close()

    def addToCSV(self, dictionary:dict, filename:str="crime.csv")   ->  None:   # Appends the values of a dictionary to a csv file
            valueList = self.getDictionaryValues(dictionary=dictionary)
            with open(file=filename, mode="a") as file:
                file.write("%s,%s,%s,%s,%s\n"%(valueList[0],valueList[1],valueList[2],valueList[3],valueList[4],))
            file.close()

    def buildCSVFile(self, amount:int=1000, filename:str="crime.csv")  -> None: # Builds a csv file with "amount" crime reports
        for x in range(amount):
            dataDict=None
            dataDict = self.createJSONCrimeReport(index=x)
            self.addToCSV(dictionary=dataDict, filename=filename)
    
    def changeFilename(self, filename:str)  ->  None:
        self.filename = filename

    def createJSONCrimeReport(self, index:int=0)   ->  dict:   # Creates a crime report as a dict
        data = self.jsonData[index]
        dictionary = {}
        dictionary["beat"] = str(data["beat"])
        dictionary["fbi_code"] = str(data["fbi_code"][:2])    # This does not take into considerations the alphabetically varitions of the FBI codes (i.e 08A -> 8)
        arrestRaw = data["arrest"]  # Boolean
        if arrestRaw:
            dictionary["arrest"] = "1"
        else:
            dictionary["arrest"] = "0"
        domesticRaw = data["domestic"]  # Boolean
        if domesticRaw:
            dictionary["domestic"] = "1"
        else:
            dictionary["domestic"] = "0"
        dictionary["district"] = str(data["district"])
        return dictionary

    def getDictionaryValues(self, dictionary:dict=None)   ->  list: # Takes a dict and spits out a list of only the values of the dict in the order that they were inputted
        return list(dictionary.values())

    def getJSONCrimeInfo(self, index:int=0) ->  dict:   # Returns a crime in raw JSON format
        return self.jsonData[index]

    def build2DList(self, amount:int=1000, remove:int=None)  ->  list:
        data = []
        removed = []
        for x in range(amount):
            dictionary = self.createJSONCrimeReport(index=x)
            values = self.getDictionaryValues(dictionary=dictionary)
            if remove is not None:
                removed.append(values.pop(remove))
            data.append(values)
        return {"DATA": data, "REMOVED": removed}

    def buildNumpyArray(self, array:list=None):
        return numpy.array(object=array)

