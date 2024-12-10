from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

sizes = [int(s) for s in lines[0]]
disk = []
empty = False
next = 0
for s in sizes:
    if empty:
        for _ in range(s):
            disk.append(-1)
    else:
        for _ in range(s):
            disk.append(next)
        next += 1
    empty = not empty
nextEmpty = sizes[0]
nextFilled = -1
while nextEmpty < len(disk) + nextFilled:
    disk[nextEmpty] = disk[nextFilled]
    while disk[nextEmpty] != -1:
        nextEmpty += 1
    nextFilled -= 1
    while disk[nextFilled] == -1:
        nextFilled -= 1
sum = 0
for i in range(len(disk) + nextFilled + 1):
    sum += i * disk[i]
print(sum)