# Lahman-to-Elasticsearch

Python utilities to convert the Lahman baseball database to JSON format and push to Elasticsearch. Baseball statistics provided by [Sean Lahman's baseball database](http://www.seanlahman.com/baseball-archive/statistics/).

Steps:
- CSV data is put into a local SQLite database 
- Run SQL queries to obtain player data
- Iterate over each player and obtain statistics. Player data + statistics are cleaned and put into a single document per player.
- All player data put into a JSON file
- JSON file is iterated upon to batch push to an Elasticsearch index
