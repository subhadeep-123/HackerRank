_, s1 = int(input()), set(map(int, input().split()))
_, s2 = int(input()), set(map(int, input().split()))
print(len(s1.symmetric_difference(s2)))
