from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

total = 0
for line in lines:
    sn = int(line)
    for i in range(2000):
        sn = sn ^ (sn << 6) % (2**24)
        sn = sn ^ (sn >> 5)
        sn = sn ^ (sn << 11) % (2**24)
    total += sn
print(total)