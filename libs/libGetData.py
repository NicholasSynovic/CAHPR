import json

import numpy


class GetData:
    def __init__(self, filename: str) -> None:
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
        self.parsedDict[key] = value

    def getCrimeSpecificInfo(self, index: int = 0, key: str = "") -> dict:
        crime = self.getSpecificCrime(index=index)
        try:
            return {key: crime[key]}
        except KeyError:  # Invalid key inputted
            print("Invalid key: " + str(key) + ", " + self.filename)
            quit(code=1)

    def getData(self) -> list:
        return self.data

    def getFilename(self) -> str:
        return self.filename

    def getKeys(self, dictionary: dict) -> list:
        return list(dictionary.keys())

    def getParsedDict(self) -> dict:
        return self.parsedDict

    def getSpecificCrime(self, index: int = 0) -> dict:
        return self.getData()[index]

    def getValues(self, dictionary: dict) -> list:
        return list(dictionary.values())

    def setData(self, filename: str = None) -> None:
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
        self.filename = filename

    def setParsedDict(self, data: dict) -> None:
        self.parsedDict = data

    def makeNumpyArray(self, amount: int) -> numpy.array:
        keys = ["beat", "community_area", "year"]
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

    def buildNumpyArray(self, amount: int, key: str, sort: bool = False) -> numpy.array:
        root = []
        for x in range(amount):
            data = self.getCrimeSpecificInfo(index=x, key=str(key))
            value = self.getValues(dictionary=data)
            root.insert(x, str(value[0]))
        if sort:
            root = sorted(root)
        return numpy.array(object=root)
