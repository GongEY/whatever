val = input()
a = 0

lst = list(map(int, raw_input().split()))
for i in range(len(lst)):
    for k in range(len(lst)):
        if i+k >= len(lst):
            continue
        else:
            a += abs(lst[i+k]-lst[i])

print(a*2)
