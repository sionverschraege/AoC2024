from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

minSaved = 70 if test else 100

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'S':
            start = (x,y)
        elif lines[y][x] == 'E':
            end = (x,y)

toEnd = [[2**20 for c in line] for line in lines]
current = end
last = end
currentDist = 0
while current != None:
    x,y = current
    toEnd[y][x] = currentDist
    currentDist += 1
    next = None
    for d in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx = x + d[0]
        ny = y + d[1]
        if (nx,ny) != last and lines[ny][nx] != '#':
            next = (nx,ny)
    last = current
    current = next

cheats = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if toEnd[y][x] < 2**20:
            for dx in range(-20,21):
                dyMax = 20 - abs(dx)
                for dy in range(-dyMax, dyMax+1):
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and ny >= 0 and ny < len(lines) and nx < len(lines[y]) and toEnd[y][x] - toEnd[ny][nx] - abs(dx) - abs(dy) >= minSaved:
                        cheats += 1

print(cheats)