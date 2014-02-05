# mchizzle
from subprocess import call
import json
from pprint import pprint
import sys
# arguments - 3 json files (op), map name (opt), player name (opt)
def main(*args):
    # creates variables depending on if argument is available
    one = args[1] if (len(args) > 1) else "json/one.json"
    """"
    two = args[2] if (len(args) > 2) else "json/two.json"
    three = args[3] if (len(args) > 3) else "json/three.json"
    """
    mapName = args[4] if (len(args) > 4) else "minecraft/flatland"
    playerName = args[5] if (len(args) > 5) else "Player"
    """
    json_one = open(one)
    one_data = json.load(json_one)
    json_one.close()
    
    json_two = open(two)
    two_data = json.load(json_two)
    json_two.close()

    json_two = open(three)
    json_data = json.load(json_three)
    json_three.close()
   """	    
    runTool(mapName) 
    createObject(one, playerName) 
    exportMap()
    cleanMap()

def createObject(data, playerName):
    

# runs command line minecraft editor in shell
def runTool(mapName):    
    call(["python", "mce.py", mapName])

# cleans map 
def cleanMap():
    call(["clean"])


main(sys.argv)


