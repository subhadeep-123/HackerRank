num = int(input())

result = 0
maximun = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximun:
            maximun = result

    else:
        result = 0

    num //= 2
print(maximun)
