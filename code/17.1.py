from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

regs = [int(l.split()[2]) for l in lines[:3]]
codes = [int(p) for p in lines[4].split()[1].split(',')]
ptr = 0
out = []
while ptr < len(codes) - 1:
    lval = codes[ptr+1]
    cval = lval if lval < 4 else regs[lval-4]
    match codes[ptr]:
        case 0:
            regs[0] = regs[0] >> cval
        case 1:
            regs[1] = regs[1] ^ lval
        case 2:
            regs[1] = cval % 8
        case 3:
            if regs[0] != 0:
                ptr = lval - 2
        case 4:
            regs[1] = regs[1] ^ regs[2]
        case 5:
            out.append(str(cval % 8))
        case 6:
            regs[1] = regs[0] >> cval
        case 7:
            regs[2] = regs[0] >> cval
    ptr += 2
print(','.join(out))