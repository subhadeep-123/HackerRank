n, x = map(int, input().split())
sheet = []
for _ in range(x):
    sheet.append(map(int, input().split()))

for i in zip(*sheet):
    print(sum(i) / len(i))
