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
  - An SQLite database is created along with tables defined in the `/sql` directory
  - CSV data from the Lahman Databae is imported into the local SQLite database 
  - SQL queries obtain base player information. For each player, their career statistics are SELECTed, cleaned, and put into a single document.
  - All player data put into a JSON file
  - Data from the JSON file is batch pushed to Elasticserch
