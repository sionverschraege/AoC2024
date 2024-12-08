from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

orders = {}
initDone = False
total = 0
for line in lines:
    if line == '':
        initDone = True
    elif initDone:
        ok = True
        pages = line.split(',')
        forbidden = set()
        for p in pages:
            if p in orders.keys():
                for o in orders[p]:
                    forbidden.add(o) 
            if p in forbidden:
                ok = False
                break
        if not ok:
            np = []
            todo = set(pages)
            while len(todo) > 0:
                next = todo.pop()
                changed = True
                while changed:
                    changed = False
                    for op in todo:
                        if next in orders.keys() and op in orders[next]:
                            changed = True
                            todo.add(next)
                            todo.remove(op)
                            next = op
                            break
                np.append(next)
            total += int(np[len(np)//2])

    else:
        f,s = line.split('|')
        if s not in orders.keys():
            orders[s] = set()
        orders[s].add(f)

print(total)
