"""5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39"""

#n = int(input())
studs = [['Harry', 37.21], ['Berry', 37.21], [
    'Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
#cols = []

"""for i in range(n):
    cols = input().split()
    cols[1] = int(cols[1])
    studs.append(cols)
print(studs)"""

studs.sort(key=lambda x: x[1])
print(studs)
