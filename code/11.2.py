from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

nums = [int(n) for n in lines[0].split()]
cache = {}

toCheck = nums
for i in range(75):
    next = []
    for n in toCheck:
        if n not in cache.keys():
            b = []
            if n == 0:
                b = [1]
            else:
                sn = str(n)
                if len(sn) % 2 == 0:
                    b = [int(sn[:len(sn)//2]),int(sn[len(sn)//2:])]
                else:
                    b = [n*2024]
            cache[n] = b
            next += b
    toCheck = next

nums = {k:1 for k in nums}
for i in range(75):
    newNums = {}
    for k in nums.keys():
        for n in cache[k]:
            if n not in newNums.keys():
                newNums[n] = 0
            newNums[n] += nums[k]
    nums = newNums
print(sum(nums.values()))