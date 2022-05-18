from bs4 import BeautifulSoup
import requests
import pdb
from collections import OrderedDict
import json


URL = "https://wiki.tppc.info/Pokemon"

def get_pokedex():
    pokedex = OrderedDict()
    page = requests.get(URL)
    content = BeautifulSoup(page.content, "html.parser")
    pokemon = content.find_all('tr')[1::]
    for poke in pokemon:
        try:
            elements = [y for y in [x for x in poke.children][3]]
            if len(elements) < 3:
                continue
            image_id = elements[1]["alt"].strip(".gif")
            name = elements[3]["title"]
            if len(elements) > 5:
                name += " " + elements[5].text
            pokedex[image_id] = name
        except Exception as e:
            pdb.set_trace()
    return pokedex


if __name__ == "__main__":
    pokedex = get_pokedex()
    json.dump(pokedex, open("pokedex.json", "w"), indent=4)
    pdb.set_trace()