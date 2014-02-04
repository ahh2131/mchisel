# mchisel
from subprocess import call
import json
from pprint import pprint

# arguments - 3 json files (op), map name (opt), player name (opt)
def main(*args):
    # creates variables depending on if argument is available
    one = args[0] if args[0] else "json/one.json"
    two = args[1] if args[1] else "json/two.json"
    three = args[2] if args[2] else "json/three.json"
    mapName = args[3] if args[3] else "map/level.dat"
    playerName = args[4] if args[4] else "Player"

    json_one = open(one)
    one_data = json.load(json_one)
    json_one.close()
    
    json_two = open(two)
    two_data = json.load(json_two)
    json_two.close()

    json_two = open(three)
    json_data = json.load(json_three)
    json_three.close()
  	    
    runTool(mapName, playerName)
    

# runs command line minecraft editor in shell
def runTool(mapName, playerName):    

main(*args)


