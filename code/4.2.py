from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

toprint = [[False for _ in row] for row in lines]
count = [[0 for _ in row] for row in lines]
total = 0
mas = "MAS"
for y in range(1,len(lines)-1):
    for x in range(1,len(lines[0])-1):
        if lines[y][x] == 'A':
            for dx in [-1,1]:
                for dy in [-1,1]:
                    #if x - 1 >= 0 and y - 1 >= 0 and x + 1 < len(lines[y]) and y + 1 < len(lines)
                    if lines[y+dy][x+dx] == 'M' and lines[y-dy][x-dx] == 'S' \
                    and lines[y+dx][x-dy] == 'M' and lines[y-dx][x+dy] == 'S':
                        toprint[y][x] = True
                        toprint[y+dy][x+dx] = True
                        toprint[y-dy][x-dx] = True
                        toprint[y+dx][x-dy] = True
                        toprint[y-dx][x+dy] = True
                        total += 1
                        count[y][x] += 1
                        # if dx == 0 or dy == 0:
                        #     print('Rot',dx,dy)
                        #     for ddy in range(-1,2):
                        #         print(lines[y+ddy][x-1:x+2])
                        #     print()

# for y in range(len(lines)):
#     for x in range(len(lines[0])):
#         print(count[y][x] if toprint[y][x] else '.', end='')
#     print()
print(total)
# 1953 too high