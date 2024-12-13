from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

tokens = 0
for i in range(0, len(lines), 4):
    ax,ay = [int(w.split('+')[1].split(',')[0]) for w in lines[i].split()[2:4]]
    bx,by = [int(w.split('+')[1].split(',')[0]) for w in lines[i+1].split()[2:4]]
    px,py = [int(w.split('=')[1].split(',')[0]) for w in lines[i+2].split()[1:3]]
    
    if ax*by == bx*ay:
        print(f'({ax},{ay}) and ({bx},{by}) not linearly independent')
    else:
        # line a from 0,0 to intercept
        # line b from intercept to px,py
        # nax + mbx = px
        # nay + mby = py
        # naxay + mbxay = pxay
        # nayax + mbyax = pyax
        # mbxay - mbyax = pxay - pyax
        # m = (pxay - pyax) / (bxay - byax)
        # n = (pxby - pybx) / (axby - aybx)
        m = (px*ay - py*ax) // (bx*ay - by*ax)
        n = (px*by - py*bx) // (ax*by - ay*bx)
        if n*ax + m*bx == px and n*ay + m*by == py and n <= 100 and m <= 100:
            tokens += 3*n + m
print(tokens)