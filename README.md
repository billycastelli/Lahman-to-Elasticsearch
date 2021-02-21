# Lahman-to-Elasticsearch

Python utilities to convert the Lahman baseball database to JSON format and push to Elasticsearch. Baseball statistics provided by [Sean Lahman's baseball database](http://www.seanlahman.com/baseball-archive/statistics/).

Running this program will add 20,000+ documents to an Elasticsearch index which can be used for searching or data analysis. Currently, players are associated with data from `people.csv` and `batting.csv`. 

## Steps
Create a Python virtual environment:
```
>> python3 -m venv .
```

Install required dependencies
```
>> pip3 -r install requirements.txt
```

Add your Elasticsearch node information in a local `.env` file (see `.env.example`):
- The easiest way to spin up a local Elasticsearch node is through [Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

Run the program:
```
>> python3 baseball-stats-formatter.py
```

If all goes well, you will be able to view your documents by running a curl against `<ELASTICSEARCH_URL>/<index>/_search`

## How the program works
  Steps:
  - An SQLite database is created - tables are defined in the `/sql` directory
  - CSV data from the Lahman Databae is imported into the local SQLite database 
  - SQL queries obtain base player information. For each player, career statistics are SELECTed, cleaned, and put into a single document.
  - All player data is written to a JSON file
  - Data from the JSON file is batch pushed to Elasticsearch

The result documents in Elasticsearch will be in the following format:
```
{
    "playerID": "ruthba01",
    "birthYear": 1895,
    "birthMonth": 2,
    "birthDay": 6,
    "birthCountry": "USA",
    "birthState": "MD",
    "birthCity": "Baltimore",
    "deathYear": 1948,
    "deathMonth": 8,
    "deathDay": 16,
    "deathCountry": "USA",
    "deathState": "NY",
    "deathCity": "New York",
    "nameFirst": "Babe",
    "nameLast": "Ruth",
    "nameGiven": "George Herman",
    "weight": 215,
    "height": 74,
    "bats": "L",
    "throws": "L",
    "debut": "1914-07-11",
    "finalGame": "1935-05-30",
    "retroID": "ruthb101",
    "bbrefID": "ruthba01",
    "career_batting": {
        "games": 2503,
        "ab": 8398,
        "runs": 2174,
        "hits": 2873,
        "doubles": 506,
        "triples": 136,
        "homeruns": 714,
        "rbi": 2217,
        "sb": 123,
        "cs": 117,
        "bb": 2062,
        "so": 1330,
        "ibb": 0,
        "hbp": 43,
        "sh": 113,
        "sf": 0,
        "gidp": 2,
        "avg": "0.342"
    },
    "name": "Babe Ruth",
    "batting": [
        {
            "playerID": "ruthba01",
            "yearID": 1914,
            "stint": 1,
            "teamID": "BOS",
            "leagueID": "AL",
            "games": 5,
            "ab": 10,
            "runs": 1,
            "hits": 2,
            "doubles": 1,
            "triples": 0,
            "homeruns": 0,
            "rbi": 2,
            "sb": 0,
            "cs": "",
            "bb": 0,
            "so": 4,
            "ibb": "",
            "hbp": 0,
            "sh": 0,
            "sf": "",
            "gidp": "",
            "avg": "0.200"
        },
        { ... }, 
        { ... }
    ]
}
```

