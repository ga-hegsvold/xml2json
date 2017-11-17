# xml2json (experimental)
[![Build Status](https://travis-ci.org/sesam-community/endpoint2file.svg?branch=master)](https://travis-ci.org/sesam-community/endpoint2file)

A micro-service for reading an xml byte stream from an api and transforming it to json.

## Environment variables

`JWT` - JSON Web Token granting access to CONFIG_ENDPOINT and all ENDPOINTs defined in CONFIG_ENDPOINT

`NODE` - base url to the sesam node instance api (ex: "https://abcd1234.sesam.cloud/api")

`XML_API` - url to xml api

## Example Sesam System Config
```
{
  "_id": "xml2json-service",
  "type": "system:microservice",
  "docker": {
    "environment": {
      "JWT": "$SERCRET(JWT)",
      "NODE": "https://abcd1234.sesam.cloud/api",
      "XML_API": "https://boardgamegeek.com/xmlapi/collection/zodiac" 
    },
    "image": "some-docker-user/xml2json:latest",
    "port": 5000
  }
}
```
