# Solution 1
N, M = map(int, input().split())
for i in range(1, N, 2):
    print((i*'.|.').center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print((i*'.|.').center(M, '-'))

# Solution2
n, m = map(int, input().split())
pattern = [(i*'.|.').center(m, '-') for i in range(1, n, 2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
