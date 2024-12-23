from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

options = lines[0].split(', ')
partpossible = set()
possible = set()
for option in options:
    for i in range(len(option)):
        partial = option[:i+1]
        partpossible.add(partial)
    possible.add(option)

def isPossible(line: str) -> bool:
    if line in possible:
        return True
    i = 0
    current = line[0]
    while current in partpossible:
        i += 1
        if i >= len(line):
            return False
        if current in possible and isPossible(line[i:]):
            return True
        current += line[i]
    return False

oc = possible.copy()
while len(oc) > 0:
    o = oc.pop()
    possible.remove(o)
    if not isPossible(o):
        possible.add(o)

total = sum([isPossible(l) for l in lines[2:]])
print(total)
    