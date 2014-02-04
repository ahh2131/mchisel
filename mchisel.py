# mchisel

# arguments - 3 json files (op), map name (opt), player name (opt)
def main(*args):
    # creates variables depending on if argument is available
    one = args[0] if args[0] else "json/one.json"
    two = args[1] if args[1] else "json/two.json"
    three = args[2] if args[2] else "json/three.json"
    mapName = args[3] if args[3] else "map/level.dat"
    playerName = args[4] if args[4] else "Player"

    runTool(mapName, playerName)
        

# runs command line minecraft editor in shell
def runTool(mapName, playerName):
    

main(*args)


