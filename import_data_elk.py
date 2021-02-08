import requests
import json
from elasticsearch import Elasticsearch
import time

def mapping():
    mapping = {
        "mappings": {
            "properties": {
                "timestamp":{"type":"date"},
                "location":{"type":"geo_point"},
                "sensor_1": {"type": "float"},
                "sensor_2": {"type": "float"},
                "sensor_3": {"type": "float"},
                "sensor_4": {"type": "float"},
            }
        }
    }
    es.indices.create(index="data_generate2", ignore=400, body=mapping)
def import_data():
    r = requests.get('http://0.0.0.0:8005/')
    print(json.loads(r.text))

    doc = {
            "timestamp": json.loads(r.text)["datetimenow"],
            "location":{
                "lat":json.loads(r.text)["lat"],
                "lon":json.loads(r.text)["lon"]
                },
            "sensor_1": json.loads(r.text)["sensor_1"],
            "sensor_2": json.loads(r.text)["sensor_2"],
            "sensor_3": json.loads(r.text)["sensor_3"],
            "sensor_4": json.loads(r.text)["sensor_4"],
            }
    res = es.index(index="data_generate2", body=doc, ignore=400)

if __name__ == "__main__":

    while True:
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        #mapping()
        print("RUN")
        import_data()
        time.sleep(3)
    
    


