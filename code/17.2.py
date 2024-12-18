from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

codes = [int(p) for p in lines[4].split()[1].split(',')]

possibleAs = [0]
for code in codes[::-1]:
    npos = []
    for pa in possibleAs:
        for lsb in range(8):
            newA = 8*pa + lsb
            b = lsb ^ 5
            c = newA >> b
            b = b ^ c ^ 6
            if (b % 8) == code:
                npos.append(newA)
    possibleAs = npos
possibleAs.sort()
print(possibleAs[0])
# 120632132875995 too high
# 106007538883178 too low