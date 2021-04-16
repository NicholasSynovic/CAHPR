import json


class Generator:
    def __init__(self, key: str) -> None:

        self.key = key
        self.data = []
        self.mega = []

    def getData(self):

        return self.data

    def getDataFromFile(self, filename: str) -> None:

        with open(file=filename) as file:
            self.data = json.load(fp=file)
            file.close()

    def searchForValue(self, value) -> list:

        root = []
        for x in range(len(self.data)):
            if self.data[x][self.key] == value:
                root.insert(x, self.data[x])
        return root

    def addToList(self, data: list) -> None:

        for x in range(len(data)):
            self.mega.append(data[x])

    def writeListToFile(self, filename: str = "agregatedCrimes.json") -> None:

        with open(file=filename, mode="a") as file:
            json.dump(obj=self.mega, fp=file)
            file.close()
