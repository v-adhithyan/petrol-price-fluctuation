curl -XPUT 'http://localhost:9200/petrol' -d'
{
  "mappings": {
    "rates": {
      "properties": {
        "date": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        },
        "rate": {
          "type": "float"
        }
      }
    }
  }
}
'
