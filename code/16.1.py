from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')
import heapq

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == 'S':
            start = (x,y)
        elif lines[y][x] == 'E':
            end = (x,y)
dirs = [(1,0),(0,-1),(-1,0),(0,1)]

# estimate, done, coord, dir
pq = [(0, 0, start, 0)]
checked = set()
total = 0
while len(pq) > 0 and total == 0:
    _, done, pos, dir = heapq.heappop(pq)
    if pos == end:
        total = done
    elif (pos,dir) not in checked:
        checked.add((pos,dir))
        dirc = dirs[dir]
        nx,ny = pos[0]+dirc[0],pos[1]+dirc[1]
        if lines[ny][nx] != '#':
            next = [(done+1, (pos[0]+dirc[0],pos[1]+dirc[1]), dir)]
        else:
            next = []
        for dd in [-1,+1]:
            next.append((done+1000, pos, (dir+dd+4)%4))
        for n in next:
            ndone, npos, ndir = n
            nest = ndone
            if npos != end:
                if npos[0] == end[0]:
                    nest += min((ndir - 1 + 4) % 4, (1 - ndir + 4 % 4))*1000
                elif npos[1] == end[1]:
                    nest += min((ndir - 0 + 4) % 4, (0 - ndir + 4 % 4))*1000
                else:
                    nest += 1000 if ndir in [0,1] else 2000
                nest += abs(end[0]-npos[0]) + abs(end[1]-npos[1])
            heapq.heappush(pq, (nest, ndone, npos, ndir))
print(total)