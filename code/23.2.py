from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

connections  = {}
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

sets = []
keys = [k for k in connections.keys()]
for k in keys:
    newsets = [[k]]
    removesets = []
    v = connections.pop(k)
    for set in sets:
        sub = [o for o in set if o in v]
        if len(sub) == len(set):
            removesets.append(set)
        if len(sub) > 0:
            newsets.append(sub + [k])
    for r in removesets:
        sets.remove(r)
    sets = sets + newsets
l = max([len(s) for s in sets])
for s in sets:
    if len(s) == l:
        s.sort()
        print(','.join(s))

# This seems smarter but is way slower
# def findBestConnected(keys, connections):
#     cons = {k:connections[k].intersection(keys) for k in connections.keys()}
#     keys.sort(key = lambda x: len(cons[x]), reverse = True)
#     bestSet = set()
#     for k in keys:
#         if len(cons[k]) < len(bestSet):
#             break
#         else:
#             allConnected = True
#             for sk in cons[k]:
#                 for sk2 in cons[k]:
#                     if sk2 not in cons[sk]:
#                         allConnected = False
#                         break
#                 if not allConnected:
#                     break
#             if allConnected:
#                 bestSet = cons[k].union({k})
#             else:
#                 cb = findBestConnected([c for c in cons[k]], connections).union({k})
#                 if len(cb) > len(bestSet):
#                     bestSet = cb
#     return bestSet

# bestSet = findBestConnected([k for k in connections.keys()], connections)
# bestSet = [b for b in bestSet]
# bestSet.sort()
# print(','.join(bestSet))