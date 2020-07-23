import collections

x = int(input())
shoe_sizes = collections.Counter(map(int, input().split()))
n = int(input())
cost = 0
for _ in range(n):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        cost += price
        shoe_sizes[size] -= 1
print(cost)
