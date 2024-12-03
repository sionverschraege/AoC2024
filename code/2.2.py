from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

lines = [[int(s) for s in l.split()] for l in lines]
total = 0
for l in lines:
    found = False
    if l[0] != l[1] and abs(l[0] - l[1]) <= 3:
        arr = [l[i] != l[i+1] and (l[i] > l[i+1]) == (l[0] > l[1]) and abs(l[i] - l[i+1]) <= 3 for i in range(1, len(l) - 1)]
        if all(arr):
            found = True
    if not found:
        for el in range(len(l)):
            if not found:
                newl = l[:el] + l[el+1:]
                if newl[0] != newl[1] and abs(newl[0] - newl[1]) <= 3:
                    arr = [newl[i] != newl[i+1] and (newl[i] > newl[i+1]) == (newl[0] > newl[1]) and abs(newl[i] - newl[i+1]) <= 3 for i in range(1, len(newl) - 1)]
                    if all(arr):
                        found = True
    total += found
print(total)