studs = []
n = int(input())
for i in range(n):
    studs.append([input(), float(input())])

score = sorted(list(set([studs[x][1] for x in range(n)])))

studs = [x[0] for x in studs if x[1] == score[1]]
studs.sort()
for s in studs:
    print(s)
