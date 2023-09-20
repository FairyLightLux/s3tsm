import s3tsmDataStructure as structs
import s3tsm
import s3tsmUtilities as utils

def getListOfAttributeType(list, attribute):
    output = []
    for item in list:
        output.append(getattr(item, attribute))
    return output


def getSublistMatchingAttribute(list, attribute, value):
    try: 
        if(type(getattr(list[0], attribute)) is tuple):
            sublist = [item for item in list if getattr(item, attribute)[0] == value or getattr(item, attribute)[1] == value]
            return sublist
        else: 
            sublist = [item for item in list if getattr(item, attribute) == value]
            return sublist
    except Exception as error:
        print(f"{attribute} is not a valid attribute of {list[0].__class__.__name__}")
        
def getEntryMatchingAttribute(list, attribute, value):
    sublist = getSublistMatchingAttribute(list, attribute, value)
    if len(sublist) > 1:
        print(f"There is more than one unique {list[0].__class__.__name__} object with {attribute} = {value}")
    elif(sublist == []):
        print(f"No entry was found in the specified list with {attribute} equal to {value}")
        return None
    else:
        return sublist[0]

def printList(list):
    for item in list:
        print(item)
        
def printListStrings(list):
    try: 
        for object in list:
            print(object.returnPropertiesAsStrings())
    except Exception as error:
        print(f"Something went wrong when trying to print the list: {error}")
        
# Custom function to print a list of sets across multiple tournaments to find historical results of a single player
# This is not primary functionality so much as another way to use the data pulled from Battlefy
def listSetsGivenPlayer(userID, tournamentList, players, sets):
    for tournament in tournamentList:
        s3tsm.initialize('battlefy', tournament)
        match = utils.getEntryMatchingAttribute(players, 'userID', userID)
        if(match):                                       
            nameInTournament = match.IGN
            teamName = utils.getEntryMatchingAttribute(players, 'userID', userID).teamName
     
            playerSets = utils.getSublistMatchingAttribute(sets, 'teams', teamName)
        
            print(f"{tournament['name']}, Team: {teamName}, Name during tournament: {nameInTournament}")
            utils.printListStrings(playerSets)
            print()
            
if __name__ == "__main__":
    print("This program cannot be run alone.")
    sys.exit(0)