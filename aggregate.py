from utils import cleanAverage, careerBattingBase, cleanStat

# Functions to aggregate and join player information into dictionary format


def getPlayerDocument(p, cursor):
    """
    Return a dict object with a single player's career stats
    """
    player = dict(zip(p.keys(), p))
    print(player['playerID'])
    player['career_batting'] = careerBattingBase()
    player['name'] = f"{player['nameFirst']} {player['nameLast']}"
    player['batting'] = []
    player['fielding'] = []
    if 'debut' in player and player['debut'] == '':
        player['debut'] = None
    if 'finalGame' in player and player['finalGame'] == '':
        player['finalGame'] = None
    cursor.execute(
        f"SELECT * FROM batting where playerID = '{player['playerID']}'")
    battingLines = cursor.fetchall()
    for line in battingLines:
        line = dict(zip(line.keys(), line))
        line['avg'] = cleanAverage(line['hits'], line['ab'])
        for stat in line:
            if stat in player['career_batting']:
                player['career_batting'][stat] += cleanStat(line[stat])
        player['batting'].append(line)
        player['career_batting']['avg'] = cleanAverage(player['career_batting']['hits'],
                                                       player['career_batting']['ab'])
    return player


def getAllPlayers(playerList, cursor):
    """
    Return all player documents in list format 
    """
    allPlayers = []
    for p in playerList:
        playerDocument = getPlayerDocument(p, cursor)
        allPlayers.append(playerDocument)
    return allPlayers
