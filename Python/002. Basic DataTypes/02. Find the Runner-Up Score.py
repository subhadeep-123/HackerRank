# n is not required in this program
# to meet the requirements of STDIN of hackerrank we are using n variable
def soln(a, scores):
    scores = sorted(list(dict.fromkeys(scores)))
    print(scores[-2])


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    soln(n, arr)
