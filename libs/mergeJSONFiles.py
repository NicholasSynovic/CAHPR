from os import listdir
from os.path import join

import pandas


class MergeJSONFiles:
    def __init__(self, directory: str) -> None:
        self.directory = directory

    def getJSONFilePaths(self) -> set:

        jsonFilePaths: set = set()
        filetree: str = listdir(self.directory)

        for file in filetree:
            if file.endswith(".json"):
                jsonFilePaths.add(join(self.directory, file))

        return jsonFilePaths

    def merge(self, jsonFileSet: set) -> None:
        # https://blog.softhints.com/how-to-merge-multiple-csv-files-with-python/

        df_FromAll = (pandas.read_json(json) for json in jsonFileSet)

        try:
            df_Merged = pandas.concat(df_FromAll, ignore_index=True).drop_duplicates()
        except ValueError as ve:
            print("Concatination Failed: {}\n".format(ve))
            exit(1)
        else:
            exportLocation = join(self.dir, "_merged.json")
            print("Exporting DataFrame to JSON at {}...".format(exportLocation))
            df_Merged.to_json()(exportLocation)
