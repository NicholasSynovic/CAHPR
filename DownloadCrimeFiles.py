'''FILENAME: DownloadCrimeFiles.py
PROGRAM NAME: CPD Crime Information Downloader
CREATED BY: Nicholas M. Synovic
GITHUB: https://www.github.com/nsynovic
LAST EDITED: 4/3/2019 14:09
'''
import GetCrimes
def download(appToken:str=None, crimeRange:int=6836, startingOffset:int=0)   ->  None:
    gc = GetCrimes.GetCrimes(appToken=appToken)
    for count in range(crimeRange):
        offset = count * 1000
        if offset < startingOffset:
            pass
        else:
            filename = r"JSON\Crimes\crimes" + str(count) + ".json"
            data = gc.getURLJSON(offset=offset)
            print(str(gc.saveJSON(filename=filename, data=data)) + " " + gc.getURLString())

print("""CPD Crime Downloader
Created by Nicholas Synovic
""")
aT = input("What is your SODA app token? ")
cR = input("How many files do you want to download (NOTE: one file has a thousand crimes in it)? ")
sO = input("What is your crime offset (NOTE: enter 0 if you don't know)? ")
print("""Starting download...
""")

download(appToken=aT, crimeRange=cR, startingOffset=sO)
