import csv
import json
from aggregate import getAllPlayers
from SQLiteWrapper import SQLiteWrapper


def csvToSQLite(dbFile):
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


def createJSON(filename):
    dbName = 'baseball-db.sqlite'
    csvToSQLite(dbName)
    allPlayers = getAllPlayers(dbName)

    # Write all player information to a JSON file
    with open(filename, 'w') as jsonFile:
        json.dump(allPlayers, jsonFile, indent=4)
    print(f"{len(allPlayers)} players added to {filename}")
