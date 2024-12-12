from pathlib import Path
test = True
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
            perimeter = 0
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
                            perimeter += 1
                        else:
                            toCheck.add((nx,ny))
            total += area * perimeter
print(total)
