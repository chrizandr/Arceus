import discord
import random


data = open("rates.csv").read().split("\n")
rate_sheet = {}
header = data[0].split(",")
for r in data[1::]:
    poke = r.split(",")
    name, male, female, ungendered, genderless, info = poke
    rate_sheet[name.lower()] = {
        "name": name.strip(),
        "male": male.strip(),
        "female": female.strip(),
        "genderless": genderless.strip(),
        "ungendered": ungendered.strip(),
        "info": info.strip()
    }


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


def format_output(index_entry):
    time_elapsed = "Rates are subjective, so stfu if you don't agree."
    embed = discord.Embed(title=index_entry['name'], description=time_elapsed,
                          color=discord.Color.red())
    embed.add_field(name="Male", value=str(index_entry['male']), inline=True)
    embed.add_field(name="Female", value=str(index_entry['female']), inline=True)
    embed.add_field(name="Ungendered", value=str(index_entry['ungendered']), inline=True)
    embed.add_field(name="Genderless", value=str(index_entry['genderless']), inline=True)
    embed.add_field(name="Other Info", value=str(index_entry['info']), inline=False)
    return embed


def get_rate(pokemon):
    pokemon_name = get_pokemon_name(pokemon)
    if pokemon_name in rate_sheet:
        response = format_output(rate_sheet[pokemon_name])
    else:
        response = f"I rate it `{random.randint(0, 10)}/10`"
    return response


def rate_handler(message):
    values = message.content.split()
    # print(values)
    if len(values) > 1 and values[0] == "!rate":
        return get_rate(" ".join(values[1::]))

    else:
        return "Use this format ffs ```!rate <pokemon>```"
