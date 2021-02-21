from utils import cleanAverage, careerBattingBase, cleanStat
from SQLiteWrapper import SQLiteWrapper


# Functions to aggregate and join player information into dictionary format


def getPlayerDocument(p, cursor):
    """
    Return a dict object with a single player's career stats
    """
    player = dict(zip((x.lower() for x in p.keys()), p))
    print(player['playerid'])
    player['career_batting'] = careerBattingBase()
    player['name'] = f"{player['namefirst']} {player['namelast']}"
    player['batting'] = []
    player['fielding'] = []
    if 'debut' in player and player['debut'] == '':
        player['debut'] = None
    if 'finalgame' in player and player['finalgame'] == '':
        player['finalgame'] = None
    cursor.execute(
        f"SELECT * FROM batting where playerID = '{player['playerid']}'")
    battingLines = cursor.fetchall()
    for line in battingLines:
        line = dict(zip((x.lower() for x in line.keys()), line))
        line['avg'] = cleanAverage(line['hits'], line['ab'])
        for stat in line:
            if stat in player['career_batting']:
                player['career_batting'][stat] += cleanStat(line[stat])
        player['batting'].append(line)
        player['career_batting']['avg'] = cleanAverage(player['career_batting']['hits'],
                                                       player['career_batting']['ab'])
    return player


def getAllPlayers(dbName):
    """
    Return all player documents in list format
    """
    # Grab all player information
    allPlayers = []
    with SQLiteWrapper(dbName) as cursor:
        cursor.execute("SELECT * FROM people;")
        players = cursor.fetchall()
        for p in players:
            playerDocument = getPlayerDocument(p, cursor)
            allPlayers.append(playerDocument)
    return allPlayers
