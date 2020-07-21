_, s1 = input(), set(map(int, input().split()))

for _ in range(int(input())):
    cmd = input().split()[0]
    temp = input().split()
    cmd += '([' + ','.join(temp) + '])'
    eval('s1.' + cmd)
print(sum(s1))
