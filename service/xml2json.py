import requests
import logging
import datetime
import xmltodict
import json
import os
from flask import Flask, Response

app = Flask(__name__)


def get_api_stream(url, params=None, headers=None):
    """Fetch byte stream from an endpoint"""

    logging.debug("-> get_api_stream()")
    logging.debug("Request url: %s" % url)

    result = requests.get(url, params=params, headers=headers)

    logging.debug("Response content: %s" % result.content)
    logging.debug("<- get_api_stream()")

    return result


def xml_to_json(xml):
    """Transform xml to json"""

    logging.debug("-> xml_to_json()")

    xml_as_dict = xmltodict.parse(xml)
    xml_as_json = json.dumps(xml_as_dict)

    logging.debug("<- xml_to_json()")

    return xml_as_json


@app.route('/<path:url>')
def main(url):
    log_level = logging.getLevelName(os.environ.get('LOG_LEVEL', 'INFO'))  # default log level = INFO
    logging.basicConfig(level=log_level)  # dump log to stdout

    logging.debug(datetime.datetime.now())

    # fetch env vars
    xml_api = os.environ.get('XML_API')  # or "https://boardgamegeek.com/xmlapi/collection/Zodiac"

    xml_url = xml_api + "/" + url  # or 'https://boardgamegeek.com/xmlapi/collection/Zodiac'

    logging.info(xml_url)

    xml_response = get_api_stream(xml_url)

    # TODO: Only supports utf-8 encoded xml for now
    xml_data = xml_response.content.decode('utf-8')

    # FIXME: brute force removal of xml header for now
    xml_data = xml_data.replace('<?xml version="1.0" encoding="utf-8" standalone="yes"?>', '')

    json_data = xml_to_json(xml_data)

    logging.debug(json_data)

    return Response(json_data, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
