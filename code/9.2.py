from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

sizes = [int(s) for s in lines[0]]
taken = [0 for _ in sizes]
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

absPosF = len(disk) - 1
for f in range(len(sizes) - 1, 0, -2):
    absPosTg = sizes[0]
    tg = 1
    while sizes[tg] - taken[tg] < sizes[f] and tg < f:
        absPosTg += sizes[tg] + sizes[tg + 1]
        tg += 2
    if tg < f:
        for i in range(sizes[f]):
            disk[absPosTg + taken[tg] + i] = disk[absPosF - i]
            disk[absPosF - i] = -1
        taken[tg] += sizes[f]
    absPosF -= sizes[f]
    absPosF -= sizes[f-1]

sum = 0
for i in range(len(disk)):
    if disk[i] > 0:
        sum += i * disk[i]
print(sum)

# 4687549205137 too low