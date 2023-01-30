import pdb
import json

key = "SmallSmall"
key_letters = set([c for c in key])

pokedex = json.load(open("pokedex.json"))
# max_match = 0
# names = [pokedex[poke] for poke in pokedex]
# matching = []
# for name in names:
#     letters = set([c for c in name])
#     matching.append(len(letters.intersection(key_letters)))
# final = [(x, y) for x, y in zip(names, matching)]
# final.sort(key = lambda x: x[1])
# final = final[::-1]
# print(final[0:10])
# pdb.set_trace()


s = "0101 0050 0032 0056 0003 0019 0022 0016 0119 0135 0149 0092 0077 0134 0062 0012 " +\
    "0049 0060 0033 0055 0002 0088 0071 0146 0034 0083 0063 0039 0099 0111 0036 0040 " +\
    "0041 0057 0052 0095 0074 0078 0082 0143 0094 0114 0118 0021 0110 0086 0130 0080"
s = [x[-3::] for x in s.split()]
k = [pokedex[str(x)] for x in s]

pdb.set_trace()