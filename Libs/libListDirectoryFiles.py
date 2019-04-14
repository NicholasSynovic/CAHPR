import os


class GetFiles:

    def __init__(self, directory: str) -> None:
        self.directory = directory
        self.data = []

    def getData(self) -> list:
        return self.data

    def setData(self, data: list) -> None:
        self.data = data

    def getDirectory(self) -> str:
        return self.directory

    def setDirectory(self, directory: str) -> None:
        self.directory = directory

    def getDataLength(self) -> int:
        return len(self.data)

    def getListLength(self, data: list) -> int:
        return len(data)

    def getFileList(self) -> list:
        # https://stackabuse.com/python-list-files-in-a-directory/
        data = []
        for root, dirs, files in os.walk(self.directory):
            for x in range(len(files)):
                data.append(files[x])
        return data
