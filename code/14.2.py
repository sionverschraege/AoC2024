from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

w = 101
hw = w//2
h = 103
hh = h//2
its = 7000
robots = []
for line in lines:
    robots.append([[int(n) for n in w.split('=')[1].split(',')] for w in line.split()])

for i in range(its):
    taken = set()
    neighbours = 0
    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0]) % w
        robot[0][1] = (robot[0][1] + robot[1][1]) % h
        taken.add((robot[0][0], robot[0][1]))
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if (robot[0][0] + dx, robot[0][1] + dy) in taken:
                neighbours += 1
    # print(neighbours)
    if neighbours > 400:
        print('Attempt at tree, iteration',i+1)
        botset = set([(r[0][0],r[0][1]) for r in robots])
        for y in range(h):
            for x in range(w):
                print('#' if (x,y) in botset else '.', end='')
            print()
        print()