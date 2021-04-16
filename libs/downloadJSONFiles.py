import json
import requests

from progress.bar import Bar
from requests.models import HTTPError


class DownloadJSONFiles:
    def __init__(self, appToken: str) -> None:
        self.url = lambda limit, offset: "https://data.cityofchicago.org/resource/6zsd-86xi.json?$limit={}&$offset={}&$$app_token={}".format(
            limit, offset, appToken
        )

    def getJSONData(self, limit: int = 50000, maxOffset: int = 10000000) -> bool:
        fileCount = 0
        offsetAmount: int = 0
        offsetIterationRemainder: int = 0
        offsetIterations: int = maxOffset // limit
        finalOffset: int = maxOffset % limit

        if finalOffset > 0:
            offsetIterationRemainder = 1

        with Bar(
            message="Downloading JSON files",
            max=offsetIterations + offsetIterationRemainder,
        ) as bar:

            for iteration in range(offsetIterations):
                counter = 0
                while True:
                    resp = requests.get(url=self.url(limit, offsetAmount))
                    try:
                        resp.raise_for_status()
                    except HTTPError:
                        if counter < 5:
                            pass
                        else:
                            break
                    else:
                        with open(
                            file="crimes{}.json".format(fileCount), mode="w"
                        ) as file:
                            file.write(resp.json())
                            file.close()
                        break
                bar.next()
