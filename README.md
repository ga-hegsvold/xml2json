# xml2json (experimental)
A micro-service for reading an xml byte stream from an api and transforming it to json.

<!-- TODO:
## Environment variables

`XML_API` - url to xml api
-->

## Example Sesam System Config
```
{
  "_id": "xml2json",
  "type": "system:microservice",
  "docker": 
    "image": "gamh/xml2json:latest",
    "port": 5000
  }
}
```

## Example Sesam Pipe Config
```
{
  "_id": "my-boardgame-collection",
  "type": "pipe",
  "source": {
    "type": "json",
    "system": "xml2json",
    "url": "/https://boardgamegeek.com/xmlapi/collection/Zodiac"
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
