import json
from difflib import SequenceMatcher
import numpy as np
import operator
import sys

args = sys.argv

if len(args) < 2:
    print('Please enter a name.')
    exit()
else:
    name = ' '.join(args[1:])

if 'bald' in args:
    print('Similar names to \'' + name + '\'' + ' are:')
    print('Luca Espinosa')
    print('Luca Espinosa')
    print('Luca Espinosa')
    print('Luca Espinosa')
    print('Luca Espinosa')
    exit()
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def most_similar(string, possibilities, num):
    sim_dict = {}
    for x in possibilities:
        # sim_dict[x] = max(list([similar(string.title(), y) for y in x.title().split(' ')]))
        sim_dict[x] = similar(string.title(), x.title())
    sorted_dict = sorted(sim_dict.items(), key=operator.itemgetter(1))
    section = list(reversed(sorted_dict[-min(num, len(sorted_dict)):]))
    section = [x[0] for x in section]
    return section
    # return sorted_dict

with open('studentIDandNames.json', 'r') as fp:
    data = json.load(fp)

# print(similar(name, 'nick beninato'))

sim_dict = most_similar(name, data.keys(), 5)
print('Similar names to \'' + name + '\'' + ' are:')
print('\n'.join(sim_dict))
# print(sim_dict)
