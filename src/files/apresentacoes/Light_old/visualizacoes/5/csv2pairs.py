from sys import argv
from decimal import Decimal

fn = argv[1]
x = int(argv[2])
y = int(argv[3])


fp = open(fn)

pairs = '['
for line in fp:
    l = line.split(' ')
    pair = '[' + l[x].strip() + ',' + l[y].strip() + '],'
    pairs += pair
pairs = pairs[:-1] + ']'


print pairs
