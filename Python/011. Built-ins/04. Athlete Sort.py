n, m = map(int, input().split())
array = [input() for _ in range(n)]
k = int(input())

for row in sorted(array, key=lambda row: int(row.split()[k])):
    print(row)
