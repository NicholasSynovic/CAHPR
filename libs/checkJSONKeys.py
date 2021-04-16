import json
from progress.bar import Bar


class CheckJSONKeys:
    def __init__(self, filename: str, keyList: list) -> None:
        self.filename: str = filename
        self.keyList: list = keyList

        with open(filename, "r") as file:
            self.data: dict = json.load(fp=file)[0]
        file.close()

    def setData(self, filename: str) -> None:
        self.filename: str = filename
        with open(filename, "r") as file:
            self.data = json.load(file)
        file.close()

    def checkFileForFeatures(self) -> bool:
        key: str

        dataKeys: list = list(self.data.keys())

        with Bar(
            message="Checking that keys exists in {}".format(self.filename),
            max=len(self.keyList),
        ) as bar:
            for key in self.keyList:
                try:
                    dataKeys.index(key)
                    bar.next()
                except ValueError:
                    return False

        return True
