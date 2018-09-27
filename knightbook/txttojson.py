import json

mydict = {}
with open('ids.txt', 'r', encoding='utf8') as ids:
    for line in ids:
        mydict[' '.join(line.split(' ')[1:])[:-1]] = line.split(' ')[0]

print(mydict)
with open("studentIDandNames.json","w") as f:
    json.dump(mydict, f, sort_keys=True, indent=4)
