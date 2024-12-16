from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

map = []
moves = ''
for line in lines:
    if len(line) > 0:
        if line[0] == '#':
            map.append([c for c in line])
        else:
            moves += line

bot = ()
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == '@':
            bot = (x,y)

dirs = {'^':(0,-1), '>':(1,0), 'v':(0,1), '<':(-1,0)}
for c in moves:
    nx,ny = [bot[i] + dirs[c][i] for i in range(2)]
    lx,ly = nx,ny
    while map[ly][lx] == 'O':
        lx += dirs[c][0]
        ly += dirs[c][1]
    if map[ly][lx] == '.':
        if map[ny][nx] == 'O':
            map[ly][lx] = 'O'
        map[ny][nx] = '@'
        map[bot[1]][bot[0]] = '.'
        bot = (nx,ny)

total = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        c = map[y][x]
        if c == 'O':
            total += 100*y+x
        print(c, end = '')
    print()
print()
print('Total:', total)
print()