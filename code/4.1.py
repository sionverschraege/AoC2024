from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

total = 0
xmas = "XMAS"
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'X':
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if x + (3*dx) >= 0 and x + (3*dx) < len(lines[y]) and y + (3*dy) >= 0 and y + (3*dy) < len(lines):
                        if all([lines[y+(i*dy)][x+(i*dx)] == xmas[i] for i in range(4)]):
                            total += 1
print(total)