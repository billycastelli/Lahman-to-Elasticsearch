import os
import csv
import json
import time
import sqlite3
from dotenv import load_dotenv, find_dotenv
from SQLiteWrapper import SQLiteWrapper
from aggregate import getAllPlayers
from indexer import jsonToElasticsearch


def createJSON(filename):
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
        with open(filename, 'w') as jsonFile:
            json.dump(allPlayers, jsonFile, indent=4)
        print(f"{len(allPlayers)} players added to {filename}")


if __name__ == "__main__":

    # Create JSON file from Lahman data
    before = time.time()
    jsonFile = "players.json"
    createJSON(jsonFile)

    # Send to an elasticsearch index
    load_dotenv(find_dotenv())
    ELASTICSEARCH_URL = os.environ["ELASTICSEARCH_URL"]
    ELASTICSEARCH_USER = os.environ["ELASTICSEARCH_USER"]
    ELASTICSEARCH_PASS = os.environ["ELASTICSEARCH_PASS"]
    ELASTICSEARCH_INDEX = os.environ["ELASTICSEARCH_INDEX"]

    jsonToElasticsearch(jsonFile, ELASTICSEARCH_URL,
                        ELASTICSEARCH_USER, ELASTICSEARCH_PASS, ELASTICSEARCH_INDEX)
    after = time.time()
    print(f"\n{after-before} seconds elapsed")
