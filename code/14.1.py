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
its = 100
robots = []
for line in lines:
    robots.append([[int(n) for n in w.split('=')[1].split(',')] for w in line.split()])

for i in range(its):
    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0]) % w
        robot[0][1] = (robot[0][1] + robot[1][1]) % h

quadrants = [0,0,0,0]
for robot in robots:
    if robot[0][0] != hw and robot[0][1] != hh:
        q = 0 if robot[0][0] < hw else 1
        q += 0 if robot[0][1] < hh else 2
        quadrants[q] += 1
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])