n = int(input())
l = []
for i in range(n):
    ans = list(map(str, input().strip().split()))
    if ((ans[0]) == 'insert'):
        l.insert(int(ans[1]), int(ans[2]))
    elif (ans[0] == 'append'):
        l.append(int(ans[1]))
    elif (ans[0] == 'pop'):
        l.pop()
    elif (ans[0] == 'remove'):
        l.remove(int(ans[1]))
    elif(ans[0] == 'sort'):
        l.sort()
    elif(ans[0] == 'reverse'):
        l.reverse()
    elif(ans[0] == 'print'):
        print(l)
    else:
        pass
