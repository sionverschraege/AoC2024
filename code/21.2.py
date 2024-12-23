from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

numpad ={'A':(2,3),'0':(1,3)}
for x in range(3):
    for y in range(3):
        numpad[str(7-(3*y)+x)] = (x,y)

dirpad = {
    '^':(1,0),
    'A':(2,0),
    '<':(0,1),
    'v':(1,1),
    '>':(2,1)
}

def fastest(costs, step, pad):
    cx,cy = pad[step[0]]
    tx,ty = pad[step[1]]
    if not costs:
        return abs(cx-tx) + abs(cy-ty) + 1
    else:
        if step[0] == step[1]:
            return 1
        cud = '^' if cy > ty else 'v'
        clr = '<' if cx > tx else '>'
        if cx == tx:
            return costs['A' + cud] + abs(cy-ty)-1 + costs[cud + 'A']
        else:
            if cy == ty:
                return costs['A' + clr] + abs(cx-tx)-1 + costs[clr + 'A']
            else:
                best = 2**100
                if step[1] not in 'A0^' or step[0] not in '147<':
                    best = min(best, costs['A' + cud] + abs(cy-ty)-1 + costs[cud + clr] + abs(cx-tx)-1 + costs[clr + 'A'])
                if step[0] not in 'A0^' or step[1] not in '147<':
                    best = min(best, costs['A' + clr] + abs(cx-tx)-1 + costs[clr + cud] + abs(cy-ty)-1 + costs[cud + 'A'])
                return best

costmap = {}
for a in dirpad.keys():
    for b in dirpad.keys():
        costmap[a + b] = fastest(None, a+b, dirpad)

for i in range(24):
    nc = {}
    for a in dirpad.keys():
        for b in dirpad.keys():
            nc[a + b] = fastest(costmap, a+b, dirpad)
    costmap = nc

total = 0
for line in lines:
    cost = fastest(costmap,'A' + line[0],numpad) + sum([fastest(costmap,line[i:i+2],numpad) for i in range(len(line) - 1)])
    print(cost, int(line[:-1]))
    total += cost * int(line[:-1])
# 134353299 too low
print(total)