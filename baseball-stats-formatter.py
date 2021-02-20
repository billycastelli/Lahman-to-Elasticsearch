from pprint import pprint
import csv
import json
import sqlite3
from SQLiteWrapper import SQLiteWrapper
from aggregate import getAllPlayers


with SQLiteWrapper('baseball-db.sqlite') as cursor:
    # Create people table in SQLite
    with open('sql/people.sql') as createPeople:
        cursor.execute(createPeople.read())

    # Create batting table in SQLite
    with open('sql/batting.sql') as createBatting:
        cursor.execute(createBatting.read())

    # Import people CSV data into SQL database
    with open("./lahman-stats-2020/core/People.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        next(csv_reader)
        cursor.executemany(
            f'INSERT OR IGNORE INTO People VALUES ({"?,"*23}?)', csv_reader)

    # Import batting CSV data into SQL database
    with open("./lahman-stats-2020/core/Batting.csv") as file:
        csv_reader = csv.reader(file, delimiter=",")
        next(csv_reader)
        cursor.executemany(
            f'INSERT OR IGNORE INTO Batting VALUES ({"?,"*21}?)', csv_reader)

    # Grab all player information
    cursor.execute("SELECT * FROM people;")
    players = cursor.fetchall()
    allPlayers = getAllPlayers(players, cursor)

    # Write all player information to a JSON file
    print(f"{len(allPlayers)} players parsed")
    jsonFileName = "players.json"
    with open(jsonFileName, 'w') as jsonFile:
        json.dump(allPlayers, jsonFile, indent=4)
    print(f"Written to {jsonFileName}")
