def loop(n):
    for i in range(1, 11):
        res = n * i
        print(f"{n} x {i} = {res}")


if __name__ == "__main__":
    n = int(input())
    loop(n)
