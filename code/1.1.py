from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = [int(num) for num in lines[i].removesuffix('\n').split('   ')]

left = [l[0] for l in lines]
right = [l[1] for l in lines]
left.sort()
right.sort()

diff = 0
for i in range(len(left)):
    diff += abs(left[i] - right[i])
print(diff)