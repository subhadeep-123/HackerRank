def soln(i):
    if(n % 2 != 0):
        print("Weird")
    else:
        if(2 <= n <= 5):
            print("Not Weird")
        elif(6 <= n <= 20):
            print("Weird")
        elif(n >= 20):
            print("Not Weird")
        else:
            pass


if __name__ == "__main__":
    n = int(input())
    soln(n)
