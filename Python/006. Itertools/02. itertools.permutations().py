import itertools
s, k = input().split()
for elements in itertools.permutations(sorted(s), int(k)):
    print(''.join(elements))
