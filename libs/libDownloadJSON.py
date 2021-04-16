import json
from urllib.request import urlopen


class NoAppToken(Exception):
    pass


class GetCrimes:
    def __init__(self, appToken: str = None, offset: int = None) -> None:
        try:
            if appToken is not None:
                self.appToken = appToken
            else:
                raise NoAppToken
            if offset is not None:
                self.offset = offset
            else:
                self.offset = 0
        except NoAppToken:
            print(
                """No application token.
Get a valid app token at: https://data.cityofchicago.org/profile/app_tokens
"""
            )
            quit(code=1)
        self.url = (
            "https://data.cityofchicago.org/resource/6zsd-86xi.json?"
            + "$$app_token="
            + self.appToken
            + "&$offset="
            + str(self.offset)
        )
        self.json = {}

    def getAppToken(self) -> str:
        return self.appToken

    def getJSON(self) -> dict:
        return self.json

    def getOffset(self) -> int:

        return self.offset

    def getURL(self) -> str:

        return self.url

    def saveJSON(self, filename: str = None, data: dict = None) -> [str, bool]:

        try:
            with open(file=filename, mode="w") as save:
                json.dump(obj=data, fp=save)
            return [filename, True]
        except IOError:
            return [filename, False]

    def setAppToken(self, appToken: str = "") -> None:

        self.appToken = appToken

    def setJSON(self) -> None:

        data = urlopen(url=self.getURL())
        self.json = json.load(fp=data)

    def setOffset(self, offset: int = 0) -> None:

        self.offset = offset

    def setURL(self, offset: int = 0) -> None:

        self.offset = offset
        self.url = (
            "https://data.cityofchicago.org/resource/6zsd-86xi.json?"
            + "$$app_token="
            + self.appToken
            + "&$offset="
            + str(self.offset)
        )
