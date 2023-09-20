class Player:
    def __init__(self, IGN, teamName, persistentPlayerID):
        self.IGN = IGN
        self.teamName = teamName
        self.userID = persistentPlayerID
        
    #Returns all non-platform-specific properties
    def returnPropertiesAsStrings(self):
       return (f"IGN: {self.IGN:20}  Team: {self.teamName}")
        

class Team:
    def __init__(self, teamName, teamID, players, captain):
        self.teamName = teamName
        self.battlefyID = teamID
        self.players = players
        self.captain = captain
        
    #Returns all non-platform-specific properties
    def returnPropertiesAsStrings(self):
        playerList = ""
        for player in self.players: 
            playerList += (f"{player.IGN:18}")
        return (f"Team: {self.teamName:30.30}  Captain: {self.captain:20}  Players: {playerList}")
        
class Bracket:
    def __init__(self, bracketName, bracketType, bracketID, setsInBracket):
        self.name = bracketName
        self.type = bracketType
        self.battlefyID = bracketID
        self.sets = setsInBracket
        pass
    
    #Returns name and type
    def returnPropertiesAsStrings(self):
        return (f"Bracket Name: {self.name:24} Type: {self.type}")

class Set:
    def __init__(self, bracketID, bracketName, matchID, roundNumber, matchNumber, teams, scoreA, scoreB, winner, matches, isBye):
        self.bracket = bracketID
        self.bracketName = bracketName
        self.battlefyID = matchID
        self.roundNumber = roundNumber
        self.matchNumber = matchNumber
        self.teams = teams
        self.scoreA = scoreA
        self.scoreB = scoreB
        self.winner = winner
        self.matches = matches
        self.isBye = isBye
        
    #Returns non-platform-specific properties
    def returnPropertiesAsStrings(self):
        return (f"Bracket: {self.bracketName:25}Match: {self.roundNumber:2}  Round: {self.matchNumber:2}  Teams: {self.teams[0]:30} {self.teams[1]:30}  Score: {self.scoreA}-{self.scoreB}")
    
class Match:
    def __init__(self, bracketID, bracketName, roundNumber, matchNumber, gameNumber, teams, winner, isBye):
        self.bracketID = bracketID
        self.bracketName = bracketName
        self.roundNumber = roundNumber
        self.matchNumber = matchNumber
        self.gameNumber = gameNumber
        self.teams = teams
        self.winner = winner
        self.isBye = isBye
        
    def returnPropertiesAsStrings(self):
        return (f"Bracket: {self.bracketName:18}  Match: {self.roundNumber:<2}  Round: {self.matchNumber:<2}  Game: {self.gameNumber:2}  Teams: {self.teams[0]:25.25}  {self.teams[1]:25.25}  Winner: {self.winner:25.25}")
       
    def setMatchData(self, matchData):
        pass

class matchData:
    pass

class playerMatchData:
    pass

if __name__ == "__main__":
    print("This program cannot be run alone.")
    sys.exit(0)