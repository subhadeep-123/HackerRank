# Solution 1
n = int(input())
a = set(map(int, input().split()))
for i in range(0, int(input())):
    com = list(map(str, input().strip().split()))
    if com[0] == 'pop':
        a.pop()
    elif com[0] == 'remove':
        a.remove(int(com[1]))
    elif com[0] == 'discard':
        a.discard(int(com[1]))
    else:
        pass
print(sum(a))

# Solution 2
n = input()
elements = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    operation = command[0]
    args = command[1:]

    if operation != 'pop':
        operation += '(' + ','.join(args) + ')'
        eval('elements.' + operation)
    else:
        elements.pop()
print(sum(elements))
