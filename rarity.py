from time import time
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
from pysondb import db
import json
import datetime
import discord
import pdb


data = db.getDb("data/rarity.json")

TIME_FORMAT = "%m/%d/%Y, %H:%M:%S"
RARITY_PAGE = "https://www.tppcrpg.net/rarity.html"
TIME_ELAPSED_FORMAT = "Updated {h} hours, {m} minutes and {s} seconds ago."
UPDATE_INTERVAL = 24

def get_rarity_index():
    page = requests.get(RARITY_PAGE)
    content = BeautifulSoup(page.content, "html.parser")
    pokemon = content.find_all('tr')[1::]

    rarity_index = dict()

    for poke in pokemon:
        poke = [x for x in list(poke.children) if type(x) is Tag]
        rank, name, male, female, genderless, ungendered, total = poke
        rarity_index[name.get_text().lower()] = {
            "name": name.get_text(),
            "rank": int(rank.get_text()),
            "male": int(male.get_text()),
            "female": int(female.get_text()),
            "genderless": int(genderless.get_text()),
            "ungendered": int(ungendered.get_text()),
            "total": int(total.get_text())
        }
    return rarity_index


def update_rarity(entry):
    print("[DEBUG]: Updating the rarity index timestamp")
    curr_time = datetime.datetime.now().strftime(TIME_FORMAT)
    rarity_index = json.dumps(get_rarity_index())
    if "rarity_timestamp" not in entry[0] or "rarity_timestamp" not in entry[0]:
        data.add({"rarity_timestamp": curr_time, "rarity_index": rarity_index})
    else:
        data.updateById(entry[0]["id"], {"rarity_timestamp": curr_time, "rarity_index": rarity_index})


def validate_format():
    entry = data.get()
    # Check if index exists in database
    if "rarity_index" not in entry[0] or "rarity_timestamp" not in entry[0]:
        update_rarity(entry)


def validate_time():
    entry = data.get()
    # Check if the index has been updated in the last 24 hours
    curr_time = datetime.datetime.now()
    rarity_timestamp = datetime.datetime.strptime(entry[0]["rarity_timestamp"], TIME_FORMAT)
    if curr_time - rarity_timestamp > datetime.timedelta(hours=UPDATE_INTERVAL):
        update_rarity(entry)


def validate_index():
    validate_format()
    validate_time()
    return data.get()


def get_pokemon_name(pokemon):
    """Covnert name to a standard format for lookup"""
    pokemon = pokemon.lower()
    if pokemon.startswith("s."):
        pokemon = pokemon.replace("s.", "shiny")
    if pokemon.startswith("d."):
        pokemon = pokemon.replace("d.", "dark")
    if pokemon.startswith("g."):
        pokemon = pokemon.replace("g.", "golden")
    return pokemon


def get_last_updated(entry):
    curr_time = datetime.datetime.now()
    rarity_timestamp = datetime.datetime.strptime(entry[0]["rarity_timestamp"], TIME_FORMAT)
    delta = curr_time - rarity_timestamp
    d = dict()
    d['h'], rem = divmod(delta.seconds, 3600)
    d['m'], d['s'] = divmod(rem, 60)
    return TIME_ELAPSED_FORMAT.format(**d)


def format_output(index_entry, entry):
    time_elapsed = get_last_updated(entry)
    embed = discord.Embed(title=index_entry['name'], description=time_elapsed,
                          color=discord.Color.orange())
    embed.add_field(name="Total", value=str(index_entry['total']), inline=False)
    embed.add_field(name="Male", value=str(index_entry['male']), inline=True)
    embed.add_field(name="Female", value=str(index_entry['female']), inline=True)
    embed.add_field(name="Ungendered", value=str(index_entry['ungendered']), inline=True)
    embed.add_field(name="Genderless", value=str(index_entry['genderless']), inline=True)
    return embed


def get_rarity(pokemon):
    entry = validate_index()
    rarity_index = json.loads(entry[0]["rarity_index"])
    pokemon_name = get_pokemon_name(pokemon)
    if pokemon_name in rarity_index:
        response = format_output(rarity_index[pokemon_name], entry)
    else:
        response = f"WTF is a `{pokemon}`"
    return response


def rarity_handler(message):
    values = message.content.split()
    # print(values)
    if len(values) > 1 and values[0] == "!rarity":
        return get_rarity(" ".join(values[1::]))

    else:
        return "Use this format ffs ```!rarity <pokemon>```"
