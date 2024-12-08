from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

ants = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != '.':
            if lines[y][x] not in ants.keys():
                ants[lines[y][x]] = []
            ants[lines[y][x]].append((x,y))

anns = set()
for v in ants.values():
    for a1 in v:
        for a2 in v:
            dx = a1[0] - a2[0]
            dy = a1[1] - a2[1]
            nx = a1[0] + dx
            ny = a1[1] + dy
            if (dx != 0 or dy != 0) and nx >= 0 and ny >= 0 and ny < len(lines) and nx < len(lines[y]):
                anns.add((nx, ny))
print(len(anns))
