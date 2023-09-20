import requests, json, sys

import s3tsmDataStructure as structs

BATTLEFY_API_URL = 'https://dtmwra1jsgyb0.cloudfront.net/'

def getOverview(tID):
    url = BATTLEFY_API_URL + 'tournaments/' + tID
    response = requests.get(url)
    data = response.json()
    return data

def getBracketData(tID, bID):
    url = BATTLEFY_API_URL + 'tournaments/' + tID + '/stages/' + bID
    response = requests.get(url)
    data = response.json()
    return data

def getSetsInBracket(bID): 
    url = BATTLEFY_API_URL + 'stages/' + bID + '/matches'
    response = requests.get(url)
    data = response.json()
    return data

def getTeams(tID):
    url = BATTLEFY_API_URL + 'tournaments/' + tID + '/teams'
    response = requests.get(url)
    data = response.json()
    return data

def parseBattlefyTournament(tournamentID):
    #tID is the first string in battlefy url after the tournament name
    tournamentOverview = getOverview(tournamentID)
    #Gets the json list of all teams in the tournament    
    teams = getTeams(tournamentID)
    
    playerList = []
    teamList = []

    #Builds a list of player and a list of teams in the tournament
    for team in teams:
        playersInTeam = []
        for player in team['players']:
            if 'userID' in player.keys():
                playerID = player['userID']
            else:
                playerID = 'NO_ID'
            currentPlayer = structs.Player(player['inGameName'], team['name'], playerID)
            playerList.append(currentPlayer)
            playersInTeam.append(currentPlayer)
            
            if 'captain' in team.keys():
                captain = team['captain']['inGameName']
            else:
                playerID = 'NO_CAPTAIN'

        currentTeam = structs.Team(team['name'], team['_id'], playersInTeam, captain)
        teamList.append(currentTeam)


    brackets = tournamentOverview['stageIDs']
    
    allSets = []
    allMatches = []
    allBrackets = []

    for bracketID in brackets:

        bracketSets = getSetsInBracket(bracketID)
        setsInBracket = []
        
        bracketInfo = getBracketData(tournamentID, bracketID)        

        for playedSet in bracketSets: 
            setMatches = []
            
            if not(playedSet['isBye']) and 'stats' in playedSet:
                for match in playedSet['stats']:
            
                    if(match['stats']['top']['winner']):
                        winner = playedSet['top']['team']['name']
                    else: 
                        winner = playedSet['bottom']['team']['name']
                    
                    currentMatch = structs.Match(bracketID, bracketInfo['name'], playedSet['roundNumber'], playedSet['matchNumber'], match['gameNumber'], (playedSet['top']['team']['name'], playedSet['bottom']['team']['name']), winner, False)
            
                    setMatches.append(currentMatch)
                    allMatches.append(currentMatch)
                
                if(playedSet['top']['winner']):
                    winner = playedSet['top']['team']['name']
                else: 
                    winner = playedSet['bottom']['team']['name']
                    
                currentSet = structs.Set(bracketID, bracketInfo['name'], playedSet['_id'], playedSet['roundNumber'], playedSet['matchNumber'], (playedSet['top']['team']['name'], playedSet['bottom']['team']['name']), playedSet['top']['score'], playedSet['bottom']['score'], winner, setMatches, False)
                setsInBracket.append(currentSet)
                allSets.append(currentSet)
                
        
        currentBracket = structs.Bracket(bracketInfo['name'], bracketInfo['bracket']['type'], bracketInfo['_id'], setsInBracket)
        allBrackets.append(currentBracket)
        
    return tournamentOverview, playerList, teamList, allSets, allMatches, allBrackets
    
    
            
    
if __name__ == "__main__":
    print("This program cannot be run alone.")
    sys.exit(0)