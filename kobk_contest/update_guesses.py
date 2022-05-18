import pdb
import json
from collections import OrderedDict

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

if __name__ == "__main__":
    # update_guesses()
    close_guesses()