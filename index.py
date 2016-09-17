from elasticsearch import Elasticsearch
import csv

es = Elasticsearch()
data = csv.DictReader(open("petrol-rates.csv"))

id = 0
for row in data:
    row['rate'] = float(row['rate'])
    es.index(index="petrol", doc_type="rates", id=id, body=row)
    id = id + 1
