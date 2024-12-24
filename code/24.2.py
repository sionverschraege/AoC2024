from pathlib import Path
test = False
path = Path(__file__)
input = open(f'{path.parent.parent.absolute()}\\input\\{path.name[:-3]}{'.test' if test else ''}')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].removesuffix('\n')

import random

switches = {'z09':'cwt','cwt':'z09',
            'jmv':'css','css':'jmv',
            'z37':'pqt','pqt':'z37',
            'z05':'gdd','gdd':'z05'}
vals = {}
trig = {}
calc = {}
for line in lines:
    if ':' in line:
        k,v = line.split(': ')
        vals[k] = v == '1'
    elif '>' in line:
        i1,op,i2,_,o = line.split()
        if o in switches:
            o = switches[o]
        for i in [i1,i2]:
            if i not in trig.keys():
                trig[i] = []
            trig[i].append(o)
        calc[o] = (i1, i2, op)

for k in vals.keys():
    vals[k] = random.choice([True, False])

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

carry = 0
for i in range(45):
    s = str(i)
    if len(s) == 1:
        s = ('0' + s) 
    expected = int(vals['x' + s]) + int(vals['y' + s]) + carry
    actual = int(vals['z' + s])
    carry = 1 if expected > 1 else 0
    if expected % 2 != actual:
        print('Error for xyz' + s)

ks = [k for k in switches.keys()]
ks.sort()
print(','.join(ks))

#   Normal operation:
#      xn ... x2 x1 x0
#      yn ... y2 y1 y0 +
# ----------------------
# zn+1 zn ... z2 z1 z0
#
# z0 = x0 XOR y0
#   -> Literally in wires
# z1 = fcg XOR pjf
#    = (y01 XOR x01) XOR (y00 AND x00)
#   -> OK
# z2 = jdc XOR kmq
#    = (x02 XOR y02) XOR (vms OR vpb)
#    = (x02 XOR y02) XOR ((fcg AND pjf) OR (y01 AND x01))

# Error diagnostic:
# z09
# Given: z08 = fqf XOR jwq
# z09 SHOULD = (x09 XOR y09) XOR ((fqf AND jwq) or (y08 AND x08))
#            = jnf XOR (tgv or cfk)
#            = jnf XOR wgh
# z09 switched with cwt

# z20
# given: z19 = crc XOR vmj
# z SHOULD = (x20 XOR y20) XOR ((crc AND vmj) OR (x19 AND y19))
#          = jmv XOR (pbd OR sjt)
#          = jmv XOR vch
# NO JMV XOR VCH
# NO JMV XOR ANYTHING
# YES VCH XOR CSS
# jmv switched with css

# z37
# given: z36 = sqq XOR fgt
# z37 SHOULD = (x37 XOR y37) XOR ((sqq AND fgt) or (x36 AND y36))
#          = vcr XOR (bmm OR gst)
#          = vcr XOR nwb
# z37 switched with pqt

# z05
# given: z04 = ngk XOR vvf
# z05 SHOULD = (x05 XOR y05) XOR ((ngk AND vvf) or (x04 AND y04))
#          = wcq XOR (hpm OR mrw)
#          = wcq XOR knc
# z05 switched with gdd

# template
# given: z =  XOR 
# z SHOULD = (x XOR y) XOR (( AND ) or (x AND y))
#          =  XOR ( OR )
#          =  XOR 
