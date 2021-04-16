import hashlib
from json import dumps
from os import mkdir
from os.path import isdir, join

import requests
from progress.bar import Bar
from requests.models import HTTPError, Response


class DownloadJSONFiles:
    def __init__(self, appToken: str, outputDirectory: str) -> None:
        self.outputDirectory: str = outputDirectory

        baseURL: str = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$limit={}&$offset={}&$$app_token={}"  # E501 Error: Line too long

        self.url: str = lambda limit, offset: baseURL.format(
            limit,
            offset,
            appToken,
        )

        if isdir(self.outputDirectory):
            pass
        else:
            mkdir(self.outputDirectory)

    def downloadJSONFiles(
        self,
        limit: int = 50000,
        maxOffset: int = 10000000,
    ) -> bool:
        def __downloader(
            limit: int, offsetAmount: int, maxRetries: int = 20
        ) -> Response:
            retries: int = 0

            while True:
                resp = requests.get(url=self.url(limit, offsetAmount))
                try:
                    resp.raise_for_status()
                except HTTPError:
                    if retries < maxRetries:
                        pass
                    else:
                        return False
                else:
                    return resp

        def __storeData(data: list, filepath: str) -> None:
            with open(
                file=join(
                    filepath,
                    "crimes_{}.json".format(
                        hashlib.sha256("".join(dumps(data)).encode()).hexdigest(),
                    ),
                ),
                mode="w",
            ) as file:
                file.write(dumps(data))
                file.close()

        offsetAmount: int = 0
        offsetIterations: int = maxOffset // limit

        if maxOffset % limit > 0:
            offsetIterations += 1

        with Bar(
            message="Downloading JSON files... ",
            max=offsetIterations,
        ) as bar:
            for _ in range(offsetIterations):
                response = __downloader(limit=limit, offsetAmount=offsetAmount)

                if response is False:
                    print(
                        "Unable to get JSON file at {}".format(
                            self.url(limit, offsetAmount)
                        )
                    )
                else:
                    offsetAmount += limit

                    __storeData(
                        data=response.json(),
                        filepath=self.outputDirectory,
                    )
                bar.next()
