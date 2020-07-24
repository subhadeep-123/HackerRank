# solution 1
for i in range(int(input())):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))


# Solution2
for i in range(int(input())):
    a, A = int(input()), set(map(int, input().split()))
    b, B = int(input()), set(map(int, input().split()))
    print(A.issubset(B))
