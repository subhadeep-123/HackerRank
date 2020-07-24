import itertools
s, k = input().split()
for length in range(1, int(k) + 1):
    for elements in itertools.combinations(sorted(s), length):
        print(''.join(elements))
