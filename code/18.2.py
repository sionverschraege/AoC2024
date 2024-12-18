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

path = {(x,0) for x in range(width)}.union({(width-1,y) for y in range(1,height)})
walls = set()
next = 0
while len(path) > 0:
    nw = tuple(int(s) for s in lines[next].split(','))
    walls.add(nw)
    next += 1
    if nw in path:
        path = set()
        pq = [(0, 0, (0,0), None)]
        parent = {}
        while len(pq) > 0 and end not in parent.keys():
            _,d,p,pr = heapq.heappop(pq)
            if p not in parent.keys():
                parent[p] = pr
                if p == end:
                    c = end
                    while c is not None:
                        path.add(c)
                        c = parent[c]
                else:
                    x,y = p
                    for dx,dy in [(0,1),(-1,0),(0,-1),(1,0)]:
                        nx = x + dx
                        ny = y + dy
                        if ny >= 0 and nx >= 0 and nx < width and ny < height and (x,y) not in walls:
                            nd = d+1
                            np = (nx, ny)
                            ne = nd + abs(nx - end[0]) + abs(ny - end[1])
                            heapq.heappush(pq, (ne, nd, np, p))
print(lines[next-1])