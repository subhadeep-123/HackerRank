k = int(input())
room_list = list(map(int, input().split()))
room_set = set(room_list)
room_list_sum = sum(room_list)
room_set_sum = sum(room_set) * k
diff = room_set_sum - room_list_sum
for i in room_set:
    if diff == ((k-1)*i):
        print(i)
        break
