from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

vals = {}
for line in lines:
    sn = int(line)
    changes = [None for i in range(2000)]
    done = set()
    for i in range(2000):
        old = sn%10
        sn = sn ^ (sn << 6) % (2**24)
        sn = sn ^ (sn >> 5)
        sn = sn ^ (sn << 11) % (2**24)
        changes[i] = sn%10 - old
        if i >= 3:
            key = tuple(changes[i-3:i+1])
            if key not in done:
                done.add(key)
                if key == (-2,2,-1,-1):
                    debug = True
                if key not in vals.keys():
                    vals[key] = 0
                vals[key] += sn % 10
print(max(vals.values()))