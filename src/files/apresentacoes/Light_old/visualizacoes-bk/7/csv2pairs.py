from sys import argv
from decimal import Decimal

fn = argv[1]
x = int(argv[2])
y = int(argv[3])
delimiter = argv[4]

fp = open(fn)

pairs = '['
for line in fp:
    l = line.split(delimiter)
    pair = "{'x':" + l[x].strip() + ", 'y':" + l[y].strip() + '},'
    pairs += pair
pairs = pairs[:-1] + ']'


print pairs
