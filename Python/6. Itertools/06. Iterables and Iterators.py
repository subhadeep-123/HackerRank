import itertools

n = int(input())
list_of_nums = list(map(str, input().split()))
k = int(input())

list_comb = list(itertools.combinations(list_of_nums, k))

a_list = [e for e in list_comb if 'a' in e]

print(len(a_list) / len(list_comb))
