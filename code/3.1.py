from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

import re

total = 0
for line in lines:
    ms = re.findall('mul\\(\\d+,\\d+\\)',line)
    for m in ms:
        fs = m[4:-1].split(',')
        total += int(fs[0])*int(fs[1])
print(total)