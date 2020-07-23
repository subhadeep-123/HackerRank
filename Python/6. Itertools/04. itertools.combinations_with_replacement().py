import itertools
s, k = input().split()
for elements in itertools.combinations_with_replacement(sorted(s), int(k)):
    print(''.join(elements))
