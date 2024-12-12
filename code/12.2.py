from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

done = [[False for c in line] for line in lines]
total = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if not done[y][x]:
            area = 0
            nsleftsides = set()
            ewtopsides = set()
            toCheck = {(x,y)}
            char = lines[y][x]
            while len(toCheck) > 0:
                cx,cy = toCheck.pop()
                if not done[cy][cx]:
                    done[cy][cx] = True
                    area += 1
                    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nx = cx + dx
                        ny = cy + dy
                        if nx < 0 or ny < 0 or ny >= len(lines) or nx >= len(lines[y]) or char != lines[ny][nx]:
                            if nx == cx:
                                onTop = cy > ny
                                ewtopsides.add((nx, max(ny,cy), onTop))
                            else:
                                onLeft = cx > nx
                                nsleftsides.add((max(nx,cx),ny, onLeft))
                        else:
                            toCheck.add((nx,ny))
            perimeter = 0
            while len(nsleftsides) > 0:
                perimeter += 1
                sx,sy,side = nsleftsides.pop()
                ny = sy-1
                while (sx,ny,side) in nsleftsides:
                    nsleftsides.remove((sx,ny,side))
                    ny -= 1
                ny = sy+1
                while (sx,ny,side) in nsleftsides:
                    nsleftsides.remove((sx,ny,side))
                    ny += 1
            while len(ewtopsides) > 0:
                perimeter += 1
                sx,sy,side = ewtopsides.pop()
                nx = sx-1
                while (nx,sy,side) in ewtopsides:
                    ewtopsides.remove((nx,sy,side))
                    nx -= 1
                nx = sx+1
                while (nx,sy,side) in ewtopsides:
                    ewtopsides.remove((nx,sy,side))
                    nx += 1
            print(char, area, perimeter)
            total += area * perimeter
print(total)
