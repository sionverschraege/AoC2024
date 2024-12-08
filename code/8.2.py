from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

ants = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != '.':
            if lines[y][x] not in ants.keys():
                ants[lines[y][x]] = []
            ants[lines[y][x]].append((x,y))

def gcd(a,b):
    if a < 0 or b < 0:
        return gcd(abs(a), abs(b))
    if a < b:
        return gcd(b,a)
    if b == 0:
        return a
    return gcd(b, a%b)

anns = set()
for v in ants.values():
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            a1 = v[i]
            a2 = v[j]
            dx = a1[0] - a2[0]
            dy = a1[1] - a2[1]
            g = gcd(dx,dy)
            if g > 1:
                dx //= g
                dy //= g
            
            nx = a1[0]
            ny = a1[1]
            while (dx != 0 or dy != 0) and nx >= 0 and ny >= 0 and ny < len(lines) and nx < len(lines[y]):
                anns.add((nx, ny))
                nx += dx
                ny += dy
            
            nx = a1[0] - dx
            ny = a1[1] - dy
            while (dx != 0 or dy != 0) and nx >= 0 and ny >= 0 and ny < len(lines) and nx < len(lines[y]):
                anns.add((nx, ny))
                nx -= dx
                ny -= dy
            
print(len(anns))