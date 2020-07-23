import itertools
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(*itertools.product(a, b))
