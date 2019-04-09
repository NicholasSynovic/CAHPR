'''FILENAME: DownloadCrimeFiles.py
CREATED BY: Nicholas M. Synovic
GITHUB URL: https://www.github.com/nsynovic

ABSTRACTION: Test application of the GetCrimes.py class GetCrimes. Really is only useful for understanding how to use the GetCrime library of code, or for building your own crime database.
'''
from GetCrimes import GetCrimes
import math

aT = input("What is your app token? ")
# oS = int(input("What offset do you want your crimes to start at? "))
oS = 0
mX = int(input("What is the maximum amount of iterations that you want this program to run (NOTE: Each iteration will create 1 file)? "))

# gc = GetCrimes(appToken=aT, offset=oS)
gc = GetCrimes(appToken=aT, offset=oS)

for x in range(mX):
    new = 0
    filename = r"JSON\Crimes\crimes" + str(x) + ".json" 
    if oS == 0:
        gc.setURL(appToken=aT, offset=x*1000)
        gc.setJSON()    # Downloads json
        data = gc.getJSON() # Makes json viewable
        outcome1 = gc.saveJSON(filename=filename, data=data)
        outcome2 = gc.getURL()
        print(str(x) + ", " + str(outcome1) + ", " + outcome2)

    # else:    
    #     gc.setJSON()    # Downloads json
    #     data = gc.getJSON() # Makes json viewable
    #     outcome1 = gc.saveJSON(filename=filename, data=data)
    #     outcome2 = gc.getURL()
    #     print(str(x) + ", " + str(outcome1) + ", " + outcome2)
    #     gc.setURL(appToken=aT, offset=((oS + 1 + x * 1000)))