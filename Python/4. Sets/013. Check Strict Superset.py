A = set(input().split())
check = True
for i in range(int(input())):
    s = set(input().split())
    if (s & A != s) or (s == A):
        check = False
        break
print(check)
