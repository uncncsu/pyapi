#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
  
        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)
      
        ## Decode the response
        got_dj = gotresp.json()

        #print(got_dj["name"])
        #print(got_dj["allegiances"][0])

        for i in range(0, len(got_dj["allegiances"])):
            print(requests.get(got_dj["allegiances"][i]).json()["name"])
        
        for i in range(0, len(got_dj["books"])):
            print(requests.get(got_dj["books"][i]).json()["name"])
            #print(f"{singlebook['books']}")


if __name__ == "__main__":
    main()
