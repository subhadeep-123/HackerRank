# More than 2 lines will result in 0 score.
for i in range(1, int(input()) + 1):
    print((10 ** i - 1) ** 2 // 81)
