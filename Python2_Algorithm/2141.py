n = input()

l = []

for i in range(n):
    l.append(tuple(map(int, raw_input().split())))

l.sort()

s = 0
m = 100000000000000
k = 0

tmp1 = l[0][0]
tmp2 = l[len(l)-1][0]+2

for i in range(tmp1, tmp2):
    if s < m and i != tmp1:
        m = s
        k = i-1
        s = 0
    else:
        s = 0
    for j in range(len(l)):
        s += abs(l[j][0]-i)*l[j][1]

if n == 1:
    print l[0][0]
else:
    print k
