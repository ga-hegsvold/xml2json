import json
import logging
import requests
import xmltodict


def get_bgg_collection(collection_url='https://boardgamegeek.com/xmlapi/collection/', user='Zodiac'):
    logging.debug("-> get_bgg_collection()")

    url = collection_url + user
    r = requests.get(url)
    o = xmltodict.parse(r.text)
    j = json.dumps(o['items']['item'])

    logging.debug("<- get_bgg_collection()")

    return j


def get_bgg_game(game_url='https://boardgamegeek.com/xmlapi/boardgame/', game_id='1'):
    logging.debug("-> get_bgg_game()")

    url = game_url + game_id
    r = requests.get(url)
    o = xmltodict.parse(r.text)
    j = json.dumps(o['boardgames']['boardgame'])

    logging.debug("<- get_bgg_game()")

    return j


if __name__ == '__main__':
    get_bgg_collection()
