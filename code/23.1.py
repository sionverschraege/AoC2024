from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

connections  = {}
sets = []
for line in lines:
    c1,c2 = line.split('-')
    if c1 not in connections.keys():
        connections[c1] = {c2}
    else:
        connections[c1].add(c2)
    if c2 not in connections.keys():
        connections[c2] = {c1}
    else:
        connections[c2].add(c1)
    for o in connections[c1]:
        if o in connections[c2]:
            sets.append((c1,c2,o))

sets = [s for s in sets if s[0][0] == 't' or s[1][0] == 't' or s[2][0] == 't']
print(len(sets))