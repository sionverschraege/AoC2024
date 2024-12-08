from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

total = 0
for line in lines:
    val,f = line.split(': ')
    fs = [int(x) for x in f.split(' ')]
    val = int(val)
    options = {fs[0]}
    for f in fs[1:]:
        nops = {o + f for o in options}
        nops = nops.union({o * f for o in options})
        options = nops
    if val in nops:
        total += val
print(total)