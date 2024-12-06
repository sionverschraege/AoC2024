from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

walls = [[c == '#' for c in row] for row in lines]
dx = 0
dy = -1
for y in range(len(lines)):
    for x in range(len(lines)):
        if lines[y][x] == '^':
            sx = x
            sy = y

def findLoop(ccx,ccy,ddx,ddy,wwx,wwy) -> bool:
    nnx = ccx + ddx
    nny = ccy + ddy
    done = set()
    while nnx >= 0 and nny >= 0 and nny < len(walls) and nnx < len(walls[ny]) and (nnx, nny, ddx, ddy) not in done:
        done.add((nnx,nny,ddx,ddy))
        if walls[nny][nnx] or (nnx == wwx and nny == wwy):
            ddx,ddy = -ddy,ddx
            nnx = ccx + ddx
            nny = ccy + ddy
        else:        
            ccx = nnx
            ccy = nny
            nnx = ccx + ddx
            nny = ccy + ddy
    return (nnx, nny, ddx, ddy) in done

cx = sx
cy = sy
nx = cx + dx
ny = cy + dy
options = set()
while nx >= 0 and ny >= 0 and ny < len(walls) and nx < len(walls[ny]):
    if walls[ny][nx]:
        dx,dy = -dy,dx
        nx = cx + dx
        ny = cy + dy
    else:
        if findLoop(sx,sy,0,-1,nx,ny):
            options.add((nx, ny))
        cx = nx
        cy = ny
        nx = cx + dx
        ny = cy + dy
print(len(options))