import os
import time
from dotenv import load_dotenv, find_dotenv
from extraction import createJSON
from indexer import jsonToElasticsearch


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    # Create JSON file from Lahman data
    before = time.time()
    jsonFile = "players.json"
    createJSON(jsonFile)

    # Send to an elasticsearch index
    ELASTICSEARCH_URL = os.environ["ELASTICSEARCH_URL"]
    ELASTICSEARCH_USER = os.environ["ELASTICSEARCH_USER"]
    ELASTICSEARCH_PASS = os.environ["ELASTICSEARCH_PASS"]
    ELASTICSEARCH_INDEX = os.environ["ELASTICSEARCH_INDEX"]

    jsonToElasticsearch(jsonFile, ELASTICSEARCH_URL,
                        ELASTICSEARCH_USER, ELASTICSEARCH_PASS, ELASTICSEARCH_INDEX)
    after = time.time()
    print(f"\n{after-before} seconds elapsed")
