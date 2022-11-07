from http import client
import pdb
import json
from collections import OrderedDict
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


type_map = {
    "shiny": "Shiny",
    "dark": "Dark",
    "golden": "Golden",
    "normal": ""
}


def update_guesses():
    current_guesses = set(open("kobk_guesses.txt").read().split("\n"))
    new_guesses = open("new_guesses.txt").read().split("\n")
    pokedex = json.load(open("pokedex.json"), object_pairs_hook=OrderedDict)

    names = []
    for guess in new_guesses:
        names.append(pokedex[guess])
    names = set(names)
    updated_guesses = list(current_guesses.union(names))
    updated_guesses.sort()
    f = open("kobk_guesses.txt", "w")
    f.write("\n".join(updated_guesses))
    f.close()

    pdb.set_trace()


def get_guesses(index, pokemons, current_guesses, window):
    if index == 0:
        new_guesses = pokemons[index:index+window+1]
    else:
        new_guesses = pokemons[index-window:index] + pokemons[index+1:index+window+1]
    new_guesses = [x for x in new_guesses if x not in current_guesses]
    return new_guesses


def close_guesses(window=2):
    current_guesses = set(open("kobk_guesses.txt").read().split("\n"))
    pokedex = json.load(open("pokedex.json"), object_pairs_hook=OrderedDict)
    pokemons = [v for k, v in pokedex.items()]
    for guess in current_guesses:
        index = pokemons.index(guess)
        if index == -1:
            print(f"Invalid guess {guess}\n")
        else:
            new_guesses = get_guesses(index, pokemons, current_guesses, window)
            if len(new_guesses) > 0:
                print(f"Pokemon {guess} | Close Guesses: {', '.join(new_guesses)}")


def get_guessed_list():
    url = "https://forums.tppc.info/showthread.php?t=629562&page={}"
    pokedex = json.load(open("pokedex.json"), object_pairs_hook=OrderedDict)
    final_list = []
    poke_list_old = []
    for i in tqdm(range(1, 1000)):
        page = url.format(i)
        content = requests.get(page)
        soup = BeautifulSoup(content.text, 'html.parser')
        poke_list = get_pokes_from_page(soup, pokedex)
        if poke_list_old == poke_list:
            break
        poke_list_old = poke_list
        final_list.extend(poke_list)
    final_list.sort(key = lambda x: x[1])
    guess_set = []
    for x in final_list:
        if x not in guess_set:
            guess_set.append(x)
    guess_set = [x[0]+x[1] for x in guess_set]
    return guess_set


def get_pokes_from_page(soup, pokedex):
    poke_list = []
    img_tags = soup.find_all('img')
    for img in img_tags:
        src = img['src']
        if "graphics.tppcrpg.net/" in src:
            dex_id = src.split("/")[-1].replace(".gif", " ").replace("M", "").replace("F", "").strip()
            try:
                poke = pokedex[dex_id]
                type_ = type_map[src.split("/")[-2]]
            except KeyError:
                print("Error for the following url", src)
                pdb.set_trace()
            poke_list.append((type_, poke))
    return poke_list


def auth_gsheet():
    scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
    file_name = 'client_key.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    client = gspread.authorize(creds)
    return client


def sheet_update(poke_list):
    client = auth_gsheet()
    sheet = client.open('Kobk Contest').sheet1
    cell_range = f"A2:A{len(poke_list)+1}"
    cells = sheet.range(cell_range)
    all_records = sheet.get_all_records()
    for i, val in enumerate(poke_list):
        cells[i].value = val
    sheet.update_cells(cells)


if __name__ == "__main__":
    # update_guesses()
    # close_guesses()
    poke_list = get_guessed_list()
    pdb.set_trace()
    sheet_update(poke_list)