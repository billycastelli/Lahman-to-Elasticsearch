import json
import uuid
from datetime import datetime
from elasticsearch import Elasticsearch, helpers


def jsonToElasticsearch(filename, url, username, password, indexname):
    """
    Iterate over JSON file of player documents. Bulk send to ES index.
    """
    es = Elasticsearch(url, http_auth=(username, password))
    if not es.indices.exists(index=indexname):
        print(f"Creating {indexname} index")
        es.indices.create(indexname)
    playerDocuments = []
    with open(filename) as jsonFile:
        playerData = json.load(jsonFile)
        for player in playerData:
            document = {
                "_id": uuid.uuid4(),
                "_index": indexname,
                "timestamp": datetime.now(),
                "player": player
            }
            playerDocuments.append(document)
    print("Bulk adding players to Elasticsearch...")
    try:
        helpers.bulk(es, playerDocuments)
        print("Successful bulk insert")
        print(es.count(index=indexname))
    except Exception as e:
        print("Error during bulk insert into Elasticsearch")
        print(str(e))
