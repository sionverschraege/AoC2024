from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

import heapq

width = 7 if test else 71
height = width
end = (width-1,height-1)
fallen = 12 if test else 1024
walls = {tuple(int(s) for s in l.split(',')) for l in lines[:fallen]}
# est, done, pos 
pq = [(0, 0, (0,0))]
done = set()
while len(pq) > 0 and end not in done:
    _,d,p = heapq.heappop(pq)
    if p not in done:
        done.add(p)
        if p == end:
            print(d)
        else:
            x,y = p
            for dx,dy in [(0,1),(-1,0),(0,-1),(1,0)]:
                nx = x + dx
                ny = y + dy
                if ny >= 0 and nx >= 0 and nx < width and ny < height and (x,y) not in walls:
                    nd = d+1
                    np = (nx, ny)
                    ne = nd + abs(nx - end[0]) + abs(ny - end[1])
                    heapq.heappush(pq, (ne, nd, np))