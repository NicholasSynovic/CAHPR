import json


class CheckJSON:
    def __init__(self, keys: list = []) -> None:
        self.keys = keys

    def getKeys(self) -> list:

        return self.keys

    def setKeys(self, keys: list = []) -> None:

        self.keys = keys

    def checkFileForFeatures(self, filename: str = "", verbose: bool = False) -> bool:
        with open(file=filename) as file:
            data = json.load(fp=file)
            file.close()
        for x in range(len(data)):
            for key in self.keys:
                if verbose:
                    try:
                        data[x][key]
                    except KeyError:
                        print(filename + " has a key error with key: " + key)
                        return ["ERROR", x]
                    print(
                        filename
                        + " has key: "
                        + key
                        + ", with value: "
                        + str(data[x][key])
                    )
                else:
                    try:
                        data[x][key]
                    except KeyError:
                        return ["ERROR", x]
        return True
