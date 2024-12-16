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
            l = []
            for c in line:
                if c == '@':
                    l.append('@')
                    l.append('.')
                elif c == 'O':
                    l.append('[')
                    l.append(']')
                else:
                    l.append(c)
                    l.append(c)
            map.append(l)
        else:
            moves += line

bot = ()
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == '@':
            bot = (x,y)

dirs = {'^':(0,-1), '>':(1,0), 'v':(0,1), '<':(-1,0)}
for c in moves:
    dir = dirs[c]
    nx,ny = [bot[i] + dir[i] for i in range(2)]
    boxesToMove = set()
    toCheckForBox = {(nx,ny)}
    canMove = True
    while canMove and len(toCheckForBox) > 0:
        pbx,pby = toCheckForBox.pop()
        pbc = map[pby][pbx]
        if pbc == '[' or pbc == ']':
            boxco = (pbx,pby)
            if pbc == ']':
                boxco = (pbx-1,pby)
            if boxco not in boxesToMove:
                boxesToMove.add(boxco)
                if c == '^':
                    toCheckForBox.add((boxco[0],boxco[1]-1))
                    toCheckForBox.add((boxco[0]+1,boxco[1]-1))
                elif c == 'v':
                    toCheckForBox.add((boxco[0],boxco[1]+1))
                    toCheckForBox.add((boxco[0]+1,boxco[1]+1))
                elif c == '>':
                    toCheckForBox.add((boxco[0]+2,boxco[1]))
                elif c == '<':
                    toCheckForBox.add((boxco[0]-1,boxco[1]))
        elif pbc == '#':
            canMove = False
    if canMove:
        for bx,by in boxesToMove:
            map[by][bx] = '.'
            map[by][bx+1] = '.'
        for bx,by in boxesToMove:
            map[by+dir[1]][bx+dir[0]] = '['
            map[by+dir[1]][bx+dir[0]+1] = ']'
        map[ny][nx] = '@'
        map[bot[1]][bot[0]] = '.'
        bot = (nx,ny)

total = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        c = map[y][x]
        if c == '[':
            total += 100*y+x
        print(c, end = '')
    print()
print()
print('Total:', total)
print()