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
    if l[0] != l[1] and abs(l[0] - l[1]) <= 3:
        arr = [l[i] != l[i+1] and (l[i] > l[i+1]) == (l[0] > l[1]) and abs(l[i] - l[i+1]) <= 3 for i in range(1, len(l) - 1)]
        if all(arr):
            total += 1
print(total)