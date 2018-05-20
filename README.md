# xml2json (experimental)
A micro service for reading an xml byte stream from an api and transforming it to JSON.

## Environment variables

`XML_API` - url to xml api

### Optional

`LOG_LEVEL` the level of logging _(default: INFO)_ (Ref: https://docs.python.org/3/howto/logging.html#logging-levels)

## Docker

Image: https://hub.docker.com/r/gamh/xml2json/

## Endpoints

The service is running on port 5000 and accepts connections to the following
endpoint:

    GET /<xml-stream>

`xml-stream` is the api endpoint to fetch data from.

## Example Sesam System Config
```
{
  "_id": "bgg",
  "type": "system:microservice",
  "docker": {
    "environment": {
      "XML_API": "https://boardgamegeek.com/xmlapi"
    },
    "image": "gamh/xml2json:latest",
    "port": 5000
  }
}
```

## Example Sesam Pipe Config
```
{
  "_id": "bgg-boardgame",
  "type": "pipe",
  "source": {
    "type": "json",
    "system": "xml2json",
    "url": "/collection/Zodiac"
  },
  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["create",
          ["apply", "create-item", "_S.items.item"]
        ]
      ],
      "create-item": [
        ["copy", "*"],
        ["add", "_id", "_S.@collid"],
        ["add", "rdf:type",
          ["ni", "bgg", "_S.@subtype"]
        ],
        ["make-ni", "boardgame", "@objectid"]
      ]
    }
  },
  "pump": {
    "cron_expression": "0 0 1 1 ?"
  }
}
```
