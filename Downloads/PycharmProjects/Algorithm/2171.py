'''
으아어려워ㅓㅏㅏㅏ
x나 y로 정렬해보기?
'''

n = input()

l = []

for i in range(n) :
    l.append(tuple(map(int, raw_input().split())))


l.append((1000000000000000000, 0))
l.sort()

s = {}
c = [(-10000000000000000, 0)]
r = 0

for i in l :
    if c[0][0] != i[0] :
        for j in range(len(c)) :
            for k in range(j + 1, len(c)) :
                if (c[j][1], c[k][1]) in s :
                    r += s[(c[j][1], c[k][1])]
                    s[(c[j][1], c[k][1])] += 1
                else :
                    s[(c[j][1], c[k][1])] = 1
        c = []
    c.append(i)


print r