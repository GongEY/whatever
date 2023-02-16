val1, val2 = map(int, input().split())
val3 = val1
lst = []
mx = 0
max_val = 0

while val3 > 0:
    val = input().rstrip()
    lst.append([int(i) for i in val])
    val = int(val)
    tmp = val
    cnt = 0
    while tmp > 0:
        tmp = int(tmp/10)
        cnt += 1
    if cnt >= mx and val >= max_val:
        mx = cnt
        max_val = val
    val3 -= 1

a = len(lst)
i = -1
while a > 0:
    i += 1
    lst[i] = lst[i]*mx
    a -= 1

lst.sort(reverse=True)

a = len(lst)
i = -1
while a > 0:
    i += 1
    k = int(len(lst[i])/mx)
    tmp_lst = lst[i]
    if max == 1:
        continue
    else :
        del tmp_lst[0 : len(lst[i])-k]
    lst[i] = tmp_lst
    a -= 1

num = val2 - val1
max_val = str(max_val)
max_lst = [int(i) for i in max_val]
for i in lst:
    if i == max_lst and num > 0:
        while num > -1:
            k = len(i)
            j = -1
            while k > 0:
                j += 1
                print(i[j]),
                k -= 1
            num -= 1
    else:
        k = len(i)
        j = -1
        while k > 0:
            j += 1
            print(i[j]),
            k -= 1

