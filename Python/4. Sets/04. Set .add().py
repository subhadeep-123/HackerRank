# Solution1
print(len(set([input() for i in range(0, int(input()))])))

# Solution2
stamps = set()
for _ in range(int(input())):
    stamps.add(input())
print(len(stamps))
