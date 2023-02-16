val = input()
lst = []

while val > 0:
    t = input()
    lst.append(t)
    val = val - 1

lst.sort()

for i in lst:
    print(i)
