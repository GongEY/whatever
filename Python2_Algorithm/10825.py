val = input()

a = []
for _ in range(val) :
    l = raw_input().split()
    l[1:] = map(int, l[1:])
    a.append([-l[1], l[2], -l[3], l[0]])

a.sort()
for i in a:
    print(i[3])
