from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

options = lines[0].split(', ')
possible = set(options)
nump = {'':1}

def numPossible(line: str) -> int:
    if line in nump.keys():
        return nump[line]
    else:
        num = 0
        for sl,rest in [(line[:i+1],line[i+1:]) for i in range(len(line))]:
            if sl in options:
                num += numPossible(rest)
        nump[line] = num
        return num

total = sum([numPossible(l) for l in lines[2:]])
print(total)