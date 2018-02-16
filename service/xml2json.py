import requests
import logging
import datetime
import xmltodict
import json
import os


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


def main():
    logging.basicConfig(level=logging.DEBUG)  # dump log to stdout
    logging.debug(datetime.datetime.now())

    # fetch env vars
#    jwt = os.environ.get('JWT')
#    node = os.environ.get('NODE')
    xml_api = os.environ.get('XML_API') or "https://boardgamegeek.com/xmlapi/collection/Zodiac"

    xml_response = get_api_stream(xml_api)
    xml_data = xml_response.content.decode('utf-8')
    json_data = xml_to_json(xml_data)

    print(json_data)


if __name__ == "__main__":
    main()
