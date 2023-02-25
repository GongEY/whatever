def bum(map_list, x, y):  # 폭탄을 돌려가며 map_list를 업데이트 한다.
    bomb = map_list[x][y]
    if bomb == 0:  # 폭탄이 없는 경우 그냥 돌아간다.
        return map_list
    else:  # 폭탄이 있는 경우 해당 지점을 다 돌려야한다.
        map_list[x][y] = 0 # 일단 폭탄 돌았으니 해당 자리는 초기화 하자!
        for i in range(1, bomb+1):
            #print(x, i)
            if x - i < 0:
                pass
            else:
                map_list = bum(map_list, x - i, y)
            if x + i >= len(map_list[0]):
                pass
            else:
                map_list = bum(map_list, x + i, y)
            #print(y, i)
            if y - i < 0:
                pass
            else:
                map_list = bum(map_list, x, y - i)
            if y + i >= len(map_list[0]):
                pass
            else:
                map_list = bum(map_list, x, y + i)
    return map_list


user_list = list(map(int, input().split(" ")))
n = user_list[0]
m = user_list[1]
k = user_list[2]
map_list = []

for i in range(n):
    map_list.append(list(map(int, input().split(" "))))
for i in range(k):
    x, y = input().split(" ")
    x = int(x) - 1
    y = int(y) - 1
    map_list = bum(map_list, x, y)

count = 0
for i in range(n):
    for j in range(n):
        if map_list[i][j] != 0:
            count += 1
print(count)