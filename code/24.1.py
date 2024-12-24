from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

vals = {}
trig = {}
calc = {}
for line in lines:
    if ':' in line:
        k,v = line.split(': ')
        vals[k] = v == '1'
    elif '>' in line:
        i1,op,i2,_,o = line.split()
        for i in [i1,i2]:
            if i not in trig.keys():
                trig[i] = []
            trig[i].append(o)
        calc[o] = (i1, i2, op)

toCheck = set()
for k in vals.keys():
    if k in trig.keys():
        for v in trig[k]:
            toCheck.add(v)
while len(toCheck) > 0:
    newToCheck = set()
    for tc in toCheck:
        if calc[tc][0] in vals.keys() and calc[tc][1] in vals.keys():
            if calc[tc][2] == 'OR':
                vals[tc] = vals[calc[tc][0]] or vals[calc[tc][1]]
            elif calc[tc][2] == 'AND':
                vals[tc] = vals[calc[tc][0]] and vals[calc[tc][1]]
            else:
                vals[tc] = vals[calc[tc][0]] != vals[calc[tc][1]]
            if tc in trig.keys():
                for ntc in trig[tc]:
                    newToCheck.add(ntc)
    toCheck = newToCheck

zkeys = [k for k in vals.keys() if k[0] == 'z']
zkeys.sort()
pow = 1
total = 0
for zk in zkeys:
    if vals[zk]:
        total += pow
    pow *= 2
print(total)