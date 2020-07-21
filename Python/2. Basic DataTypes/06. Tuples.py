def soln(n, integer_list):
    t = tuple(integer_list)
    print(hash(t))


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    soln(n, integer_list)
