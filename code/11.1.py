from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

nums = [int(n) for n in lines[0].split()]

def blink(n):
    if n == 0:
        return [1]
    else:
        sn = str(n)
        if len(sn) % 2 == 0:
            return [int(sn[:len(sn)//2]),int(sn[len(sn)//2:])]
        else:
            return [n * 2024]

for i in range(25):
    nums = sum([blink(n) for n in nums],[])

print(len(nums))