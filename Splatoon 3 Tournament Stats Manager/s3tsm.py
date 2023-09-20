import sys
import Battlefy_Scraper
import s3tsmDataStructure as structs
import s3tsmUtilities as utils

# These constants are for testing purposes to save the effort of inputting the same data each time for test runs
# PLATFORM = "battlefy"
# TID = '64ea066c9188c67daeaa2e54'

tournament = None
players = []
teams = []
sets = []
matches = []
brackets = []



def initializeFromBattlefy(bID):
    global tournament, players, teams, sets, matches, brackets
    tournament, players, teams, sets, matches, brackets = Battlefy_Scraper.parseBattlefyTournament(bID)
        
def terminal():
    print("Use 'help' to see a list of available functions.")
    print("To see more info about a specific function, use 'help' [function]")
    while(True):
        userInput = input(">").lower().split()
        #If there is no second argument passed in, makes the second argument null
        if len(userInput) == 1: userInput.append(None) 
        
        match userInput[0]:
            case "help":
                help(userInput[1])
            case "list":
                if not(userInput[1]):
                    print("Specify which list you want to print. Options are players, teams, sets, matches, and brackets.")     
                else:
                    try:
                        listToPrint = globals()[userInput[1]]
                        utils.printListStrings(listToPrint)
                    except:
                        print(f"{userInput[1]} is not a valid list")
            case "searchlist":
                if not(userInput[1]):
                    print("Specify which list you want to search. See 'help objects' or 'help searchList' for more info.")     
                else:
                    try:
                        listToSearch = globals()[userInput[1]]
                        attribute = input("Please specify the field you want to search: ")
                        value = input("Please specify the value you want to match: ")
                        subList = utils.getSublistMatchingAttribute(listToSearch, attribute, value)
                        utils.printListStrings(subList)
                    except:
                        print(f"{userInput[1]} is not a valid list")
            case "findattributeofitem":
                if not(userInput[1]):
                    print("Specify which list you want to search. Options are players, teams, sets, matches, and brackets.")     
                else:
                    try:
                        listToSearch = globals()[userInput[1]]
                        searchparamater = input("Please specify the field you want to search by: ")
                        value = input("Please specify the value you want to match: ")
                        attribute = input("Please specify the attribute you wish to receive: ")
                        item = utils.getEntryMatchingAttribute(listToSearch, searchparamater, value)
                        print(getattr(item, attribute))
                    except:
                        print(f"{userInput[1]} is not a valid list")
            case "re-initialize": 
                initialize()
            case "update":
                print("This command has not yet been implemented.")
                #update(PLATFORM, TID)
            case "quit":
                print("Exiting s3stm...")
                sys.exit(0)
            case _: 
                print("Input not recognized")

def help(arg):
    match arg: 
        case "help":
            print("Prints this help page")
        case "objects":
            print("Lists objects, their properties, and accessor methods")
            print("Useful for getting specific data where there isn't a built-in method to access it")
            print("Player: IGN, teamName, battlefyID")
            print("Team: teamName, battlefyID, players, captain")
            print("Bracket: name, type, battlefyID, sets")
            print("Set: bracketName, bracket, battlefyID, roundNumber, matchNumber, teams, scoreA, scoreB, winner, matches, isBye")
            print("Match: bracketName, bracketID, roundNumber, matchNumber, gameNumber, teams, winner, isBye")
        case "list":
            print("Prints out the specified list")
            print("Use format: list [which list], ex. 'list players'")
            print("Lists are 'players', 'teams', 'sets', 'matches', and 'brackets'")
        case "searchlist":
            print("Searches a list and prints a sublist matching a given value of an attribute")
            print("Use format: searchlist [which list]. The function will ask for attribute and value.")
            print("Lists are 'players', 'teams', 'sets', 'matches', and 'brackets'")
            print("Use 'help objects' for more info on attributes")
        case "findattributeofitem": 
            print("Finds a specific attribute value of a specific item.")
            print("Useful to find platform-specific IDs.")
            print("Use format: findattributeofitem [list].")
            print("The function will ask for attribute and value to match and the attribute to get.")
        case "re-initialize":
            print("Entirely re-initializes the tournament.")
            print("Resets all stored data.")
            print("The command 'update' is generally preferred.")
        case "update":
            print("This command has not yet been implemented.")
        case "quit":
            print("Closes the program.")
        case _:
            print("Available Functions:")
            print("help: Prints this help page")
            print("help objects: Lists objects, their properties, and accessor methods")
            print("list: Prints out the specified list")
            print("searchlist: Searches a list and prints a sublist matching a given value of an attribute")
            print("findattributeofitem: Finds a specific attribute value of a specific item.")
            print("re-initialize: Entirely resets stored data.")
            print("update: This command has not yet been implemented.")
            print("quit: Closes the program.")
            
    

def initialize(platform=None, ID=None):
    if not platform: platform = input("Please provide the platform used for the tournament: ").lower()
    match platform:
        case "battlefy": 
            if not ID: ID = input("Please provide a Battlefy tournament ID: ")
            print(f"Initializing Tournament Data From {platform.capitalize()}...")
            initializeFromBattlefy(ID)
        case "start.gg":
            print("Platform not yet supported")
        case "challonge":
            print("Platform not yet supported")
        case _: 
            print("Platform not recognized")
    
    print("Initialization complete!")



if __name__ == "__main__":
    print("Splatoon 3 Tournament Stats Manager")

    # Specific call version for testing purposes
    # initialize(PLATFORM, TID)

    initialize()

    terminal()