from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')
lines = [[int(c) for c in line] for line in lines]

starts = []
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c == 0:
            starts.append((x,y))

score = 0
for sx,sy in starts:
    current = [(sx,sy,1)]
    while len(current) > 0:
        next = {}
        for x,y,r in current:
            if lines[y][x] == 9:
                score += r
            else:
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx = x+dx
                    ny = y+dy
                    if ny >= 0 and nx >= 0 and ny < len(lines) and nx < len(lines[0]) and lines[ny][nx] == lines[y][x] + 1:
                        if (nx,ny) not in next.keys():
                            next[(nx,ny)] = 0
                        next[(nx,ny)] += r
        current = [(k[0],k[1],next[k]) for k in next.keys()]
print(score)
    