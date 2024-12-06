from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

walls = [[c == '#' for c in row] for row in lines]
walked = [[False for _ in row] for row in lines]
dx = 0
dy = -1
for y in range(len(lines)):
    for x in range(len(lines)):
        if lines[y][x] == '^':
            cx = x
            cy = y

nx = cx + dx
ny = cy + dy
while nx >= 0 and ny >= 0 and ny < len(walls) and nx < len(walls[ny]):
    walked[cy][cx] = True
    if walls[ny][nx]:
        dx,dy = -dy,dx
        nx = cx + dx
        ny = cy + dy
    else:        
        cx = nx
        cy = ny
        nx = cx + dx
        ny = cy + dy
walked[cy][cx] = True
print(sum(sum(row) for row in walked))