for i in range(int(input())):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))
